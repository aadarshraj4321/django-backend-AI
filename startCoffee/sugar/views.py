from django.shortcuts import render

# Create your views here.

def takeSugar(request):
    return render(request, "sugar/sugar.html")