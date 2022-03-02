from django.contrib import admin
from .models import Product, contact_us, Comment
# Register your models here.


admin.site.register(contact_us)
admin.site.register(Comment)



class ProductAdmin(admin.ModelAdmin):
    search_fields = ('Title',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Product, ProductAdmin)
