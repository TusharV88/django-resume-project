from django.shortcuts import render

# Create your views here.
def services(Request):
    context = {'services': 'active'}
    return render(Request, 'serv/services.html', context)
