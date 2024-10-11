from django.shortcuts import render
from .models import CoffeeSeq

# Create your views here.

def takeSugar(request):
    coffees = CoffeeSeq.objects.all()
    return render(request, "sugar/sugar.html", {"coffees": coffees})