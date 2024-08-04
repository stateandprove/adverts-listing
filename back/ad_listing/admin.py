from django.contrib import admin
from .models import Category, City, Advert


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    search_fields = ["title"]
