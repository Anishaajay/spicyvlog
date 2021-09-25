from django.db import models
from django.urls import reverse

# Create your models here.


class shop(models.Model):
    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    confirm_password = models.TextField()


class Cat(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:

        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])


class Product(models.Model):

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='product')
    description = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('item', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


