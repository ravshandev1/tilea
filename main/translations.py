from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import Gallery, Project, Why, Feature, Product, Main, About, Carousel, Character


class CustomAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class StackedAdmin(TranslationStackedInline):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(About)
class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Main)
class ItemTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Carousel)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Feature)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Character)
class ItemTranslationOptions(TranslationOptions):
    fields = ('key', 'value')


@register(Product)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Why)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Gallery)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'address')


@register(Project)
class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address', 'country')
