from django.contrib import admin
from .models import Category, Brand, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'category', 'price', 'condition', 'stock', 'is_available']
    list_filter = ['is_available', 'condition', 'category', 'brand']
    list_editable = ['price', 'stock', 'is_available']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]