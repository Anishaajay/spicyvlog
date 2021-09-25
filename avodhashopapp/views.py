from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def index(request, c_slug=None):

    c_page = None
    prodt = None

    if c_slug!=None:
        c_page = get_object_or_404(Cat, slug=c_slug)
        prodt = Product.objects.filter(category=c_page, availability=True)

    else:
        prodt = Product.objects.all().filter(availability=True)
    cat = Cat.objects.all()
    paginator = Paginator(prodt, 4)

    try:
        page = int(request.GET.get('page', '1'))

    except:
        page = 1

    try:
        pro = paginator.page(page)

    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro})


# def register(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password2 = request.POST['password2']
#
#         if password == password2:
#             user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
#             user.save()
#             print("REGISTRATION SUCCESSFUL")
#             return redirect('/')
#         else:
#             print("password not match")
#             return redirect("/")
#
#
#     else:
#
#         return render(request, 'register.html')
#

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid")
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:

                if User.objects.filter(username=username).exists():

                    messages.info(request, "USERNAME ALREADY EXISTS")
                    return redirect('register')

                elif User.objects.filter(email=email).exists():
                    messages.info(request, "EMAIL ALREADY EXISTS")
                    return redirect('register')

                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            password=password)
                    user.save()
                    print("REGISTRATION SUCCESSFUL")
                    return redirect('/')

        else:
            messages.info(request, "PASSWORD NOT MATCH!!! RE-ENTER PASSWORD")
            return redirect('register')

    else:

        return render(request, 'register.html')


def search(request):
    prod = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
        return render(request, "search.html", {'qr': query, 'pr': prod})


def item(request, c_slug, product_slug):
    try:
        prod = Product.objects.get(category__slug=c_slug, slug=product_slug)

    except Exception as e:
        raise e

    return render(request, "item.html", {'pr': prod})
