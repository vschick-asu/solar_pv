from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
def dashboard(request):
    return render(request, "dashboard.html")
def certificates(request):
    return render(request, "certificates.html")
def pv_technology(request):
    return render(request, "pv_technology.html")
def pv_modules(request):
    return render(request, "pv_modules.html")
def pv_panels(request):
    return render(request, "pv_panels.html")
def join(request):
    return render(request, "join.html")
def contact_us(request):
    return render(request, "contact_us.html")

