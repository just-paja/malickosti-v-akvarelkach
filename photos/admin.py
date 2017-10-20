from django.contrib.admin import (
    TabularInline,
)


class PhotoAdmin(TabularInline):
    fields = ('image', 'description', 'weight')
    extra = 0
    ordering = ('-weight',)
