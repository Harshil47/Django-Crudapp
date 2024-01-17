from django.contrib import admin
from .models import Orders, Customer, Product, Billing, Record, TempTable
# Register your models here.
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Billing)
admin.site.register(Record)
admin.site.register(TempTable)