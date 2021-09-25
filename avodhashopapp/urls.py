from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('<slug:c_slug>/', views.index, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.item, name='item'),
    path('search', views.search, name='search'),

]

