from django.contrib import admin

from books.models import CarModel

# Register your models here.


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'info', 'price')

