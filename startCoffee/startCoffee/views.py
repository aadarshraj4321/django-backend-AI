from django.http import HttpResponse



def home(request):
    return HttpResponse("Hola World! Home Page")



def about(request):
    return HttpResponse("<h1>Hola this is About Page</h1> <h2>this is H2 tag</h2>")