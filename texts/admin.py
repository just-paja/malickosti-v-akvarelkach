from django.contrib.admin import ModelAdmin, register

from photos.admin import PhotoAdmin
from .models import (
    AboutText,
    AboutTextPhoto,
    ContactText,
    ContactTextPhoto,
    ConditionsText,
    ConditionsTextPhoto,
)


class TextAdmin(ModelAdmin):
    list_display = (
        'name',
        'weight',
        'created',
        'modified',
    )
    ordering = ('-weight',)


class AboutTextPhotoAdmin(PhotoAdmin):
    model = AboutTextPhoto


@register(AboutText)
class AboutTextAdmin(TextAdmin):
    inlines = [AboutTextPhotoAdmin]


class ConditionsTextPhotoAdmin(PhotoAdmin):
    model = ConditionsTextPhoto


@register(ConditionsText)
class ConditionsTextAdmin(TextAdmin):
    inlines = [ConditionsTextPhotoAdmin]


class ContactTextPhotoAdmin(PhotoAdmin):
    model = ContactTextPhoto


@register(ContactText)
class ContactTextAdmin(TextAdmin):
    inlines = [ContactTextPhotoAdmin]
