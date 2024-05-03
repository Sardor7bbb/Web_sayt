from django.shortcuts import render

from books.models import CarModel


# Create your views here.


def cars_list_view(request):
    cars = CarModel.objects.all()
    context = {'cars': cars}
    return render(request, 'car.html', context)

