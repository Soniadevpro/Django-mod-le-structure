from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    return render(request, 'home')

def page1(request):
    return HttpResponse("SUPER PAGE")
def services(request):
    return render(request, "services")
def contact(request):
    return render(request, 'contact')
def services_detail(request):
    return render(request, 'services_details')
# Create your views here.
