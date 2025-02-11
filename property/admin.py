from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address',]
    readonly_fields = ['created_at']

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']

    list_filter = ['active', 'new_building', 'rooms_number', 'has_balcony']

    raw_id_fields = ['liked_by']

    inlines = [
        OwnerInline,
    ]
    exclude = ["flats"]


@admin.register(Complaint)
class ComplaintForm(admin.ModelAdmin):
    raw_id_fields = ['flat']


@admin.register(Owner)
class OwnerFrom(admin.ModelAdmin):
    search_fields = ['pure_phone', 'name',]
    raw_id_fields = ['flats']
