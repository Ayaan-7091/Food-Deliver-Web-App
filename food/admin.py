from django.contrib import admin
from .models import Category,Food,OrderTable
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','url','add_date')
    search_fields=('title',)



class FoodAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=10




admin.site.register(Category,CategoryAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(OrderTable)