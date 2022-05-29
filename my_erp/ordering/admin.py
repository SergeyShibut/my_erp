from django.contrib import admin
from . import models


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customers_mame', 'customers_contact_person', 'customers_address')
    list_display_links = ('customers_address',)
    search_fields = ('customers_mame',)
    list_filter = ('customers_mame',)
    list_editable = ('customers_mame', 'customers_contact_person',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name_of_goods', 'date_of_contract', 'date_of_delivery', 'contract_status')
    list_display_links = ('contract_status',)
    search_fields = ('name_of_goods',)
    list_filter = ('name_of_goods',)
    list_editable = ('name_of_goods', 'date_of_contract', 'date_of_delivery',)


class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('docs', 'text')
    list_display_links = ('docs',)
    list_editable = ('text',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    list_display_links = ('author',)
    search_fields = ('author',)
    list_filter = ('author',)
    list_editable = ('text',)


admin.site.register(models.Customers, CustomersAdmin)
admin.site.register(models.Orders, OrdersAdmin)
admin.site.register(models.Requirements, RequirementsAdmin)
admin.site.register(models.Comments, CommentsAdmin)
