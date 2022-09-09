from django.contrib import admin
from .models import Profile, Product, SelectedProduct, CustomerDetail, Background
# Register your models here.

admin.site.register(Profile)
admin.site.register(Background)
admin.site.register(Product)
admin.site.register(SelectedProduct)
admin.site.register(CustomerDetail)
