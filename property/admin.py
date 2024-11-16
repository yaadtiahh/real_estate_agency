from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address',]
    readonly_fields = ['created_at']

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']

    list_filter = ['active', 'new_building', 'rooms_number', 'has_balcony']


admin.site.register(Flat, FlatAdmin)
