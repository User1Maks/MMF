from django.contrib import admin

from .models import Status, OperationType, Category, Subcategory


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)
