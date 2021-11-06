from django.urls import path
from . import views
app_name = 'backend'
urlpatterns = [ 
    path('product/', views.ProductListView.as_view(), name='product_list'), 
    path('certificate/', views.CertificateListView.as_view(), name='certificate_list'), 
    path('service/', views.ServiceListView.as_view(), name='service_list'), 
    path('product/<pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('certificate/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
    path('service/<pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
]

