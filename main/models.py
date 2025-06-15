from django.db import models
from .utils import generate_unique_filename
from ckeditor.fields import RichTextField


class Client(models.Model):
    image = models.ImageField(upload_to=generate_unique_filename)

    def __str__(self):
        return self.image.name


class Gallery(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to=generate_unique_filename)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.image.name


class Project(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to=generate_unique_filename)
    description = models.TextField()
    address = models.TextField()
    country = models.CharField(max_length=300)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Why(models.Model):
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to=generate_unique_filename)
    description = models.TextField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to=generate_unique_filename)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    youtube_link = models.CharField(max_length=300)
    description = RichTextField()

    def __str__(self):
        return self.name


class Character(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'characters')
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)

    def __str__(self):
        return self.product.name


class Image(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'images')
    image = models.ImageField(upload_to=generate_unique_filename)

    def __str__(self):
        return self.product.name


class Main(models.Model):
    title = models.CharField(max_length=300)
    video = models.FileField(upload_to=generate_unique_filename)
    year_of_traditions = models.IntegerField()
    countries = models.IntegerField()
    projects = models.IntegerField()
    clients = models.IntegerField()
    facebook_link = models.CharField(max_length=300)
    telegram_link = models.CharField(max_length=300)
    youtube_link = models.CharField(max_length=300)
    whatsapp_link = models.CharField(max_length=300)
    instagram_link = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Phone(models.Model):
    phone = models.CharField(max_length=300)

    def __str__(self):
        return self.phone


class About(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.title


class Carousel(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to=generate_unique_filename)

    def __str__(self):
        return self.name
