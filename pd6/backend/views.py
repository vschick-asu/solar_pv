from django.shortcuts import render
from django.db import models
from models import Model
from django.views.generic import TemplateView, ListView
from Model import Certificates

def contact(request): 
    assert isinstance(request, HttpRequest) 

    certificate_list = Model.objects.order_by('id') 

    return render(
    thing = "testing123"    
    request, 
    'certificates.html', 
#      {
#         'title':'Contact', 
#         'message':'Your contact page.',
#         'year':datetime.now().year, 
#         'contact_list': contact_list,
#      }
   )
