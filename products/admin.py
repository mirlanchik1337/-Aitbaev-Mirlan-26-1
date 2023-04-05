from django.contrib import admin
from products.models import Products, Comment


# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["title", ]
    list_display = ["title", "rate", "price"]


admin.site.register(Comment)
