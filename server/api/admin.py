from django.contrib import admin

from .models import Category, Vendor, Collection, Tag, Option, Variant, VariantOption, Image, Organize, Product, Countries, Inventory, Order, WishList


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    search_fields = ('name',)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    search_fields = ('name',)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ( 'label',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ( 'label',)


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ( 'label',)
   


@admin.register(VariantOption)
class VariantOptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'variant')
    list_filter = ('option', 'variant')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Organize)
class OrganizeAdmin(admin.ModelAdmin):
    list_display = ('category', 'collection', 'vendor')
    list_filter = ('category', 'collection', 'vendor')
    raw_id_fields = ('tags',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'brand',
        'description',
        'price',
        'thumbnail',
        'organize',
    )
    list_filter = ('organize',)
    raw_id_fields = ('images', 'variants')


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        
        'regular_pricing',
        'sale_pricing',
        'stock',
        'shipping_type',
        'global_delivery',
        'fragile_product',
        'biodegradable',
        'frozen_product',
        'expiry_date',
        'product',
    )
    list_filter = (
        'fragile_product',
        'biodegradable',
        'frozen_product',
        'expiry_date',
        'product',
    )
    raw_id_fields = ('countries',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
      
        'date',
        'customer',
        'email',
        'fulfillment_status',
        'delivery_type',
        'countries',
    )
    list_filter = ('date', 'customer', 'countries')
    raw_id_fields = ('products',)


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    list_filter = ('customer',)
    raw_id_fields = ('products',)
