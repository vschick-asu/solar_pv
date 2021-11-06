from rest_framework import serializers
from ..models import Product
from ..models import Certificate
from ..models import Service
class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = ['id', 'modelNumber', 'length', 'weight', 'cell_area', 'cell_technology', 'total_number_of_cells', 'total_number_of_cells_in_series', 'number_of_series_strings', 'nuber_of_bypass_diodes', 'series_fuse_rating', 'interconnect_material', 'interconnect_supplier', 'superstrate_type']
class CertificateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Certificate
        fields = ['id', 'userID', 'report_number', 'issue_date']
class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Service
        fields = ['id', 'service_name', 'description', 'is_fi_required']
