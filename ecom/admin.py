from django.contrib import admin
from .models import Customer,Product,Orders,Feedback,Return,Categories
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)

class ReturnAdmin(admin.ModelAdmin):
    pass
admin.site.register(Return, ReturnAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categories, CategoriesAdmin)
# Register your models here.
