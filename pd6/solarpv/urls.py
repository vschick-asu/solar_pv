from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('certificates', views.certificates, name='certificates'),
    path('join', views.join, name='join'),
    path('pv_technology', views.pv_technology, name='pv_technology'),
    path('pv_modules', views.pv_modules, name='pv_modules'),
    path('pv_panels', views.pv_panels, name='pv_panels'),
    path('contact_us', views.contact_us, name='contact_us'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
