from django.contrib import admin
from django.utils.html import format_html
from .translations import CustomAdmin
from .models import About, Client, Gallery, Carousel, Project, Client, Why, Product, Feature, Image, \
    Phone, Main


@admin.register(Project)
class ProjectAdmin(CustomAdmin):
    list_display = ("name", "address", 'country', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Why)
class WhyAdmin(CustomAdmin):
    list_display = ['name', 'description', 'display_image']

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Feature)
class FeatureAdmin(CustomAdmin):
    list_display = ['name', 'description', 'display_image']

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_image']

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

    def get_max_num(self, request, obj=None, **kwargs):
        return 4  # Maksimal 4 ta ruxsat beriladi


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone']


@admin.register(About)
class AboutAdmin(CustomAdmin):
    list_display = ('title', 'text')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True


@admin.register(Gallery)
class GalleryAdmin(CustomAdmin):
    list_display = ('name', 'address', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Product)
class ProductAdmin(CustomAdmin):
    list_display = ('name', 'display_image', 'model')
    inlines = [ImageInline]

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.images.first().image.url)


@admin.register(Carousel)
class CarouselAdmin(CustomAdmin):
    list_display = ('name', 'display_image')

    @staticmethod
    def display_image(obj):
        return format_html('<img src="{}" width="200" height="200" />', obj.image.url)


@admin.register(Main)
class MainAdmin(CustomAdmin):
    list_display = ('title', 'email')
