from django.shortcuts import render, HttpResponse


# Create your views here.
# This is functiion for home view
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Sonu Kumar'

    args = {'myname': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)
