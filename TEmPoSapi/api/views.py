from django.shortcuts import render
from api.models import CustomUser, Product, Brand, Customer, Transaction, ProductImage, Supplier, Department, Task
from api.serializers import UserSerializer, ProductSerializer, ProductImageSerializer, BrandSerializer, CustomerSerializer, TransactionSerializer, SupplierSerializer, DepartmentSerializer, TaskSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin

from django.db import models as django_models

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

class Object(CsrfExemptMixin, APIView):
    authentication_classes = []

    def post(self, request,format=None):
        return Response({'received data': request.data})

#Provides the root for the api,
#add new objects as required
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'brands': reverse('brand-list', request=request, format=format),
        'productimages': reverse('brand-list', request=request, format=format)
    })


#Creates views for Users (Custom user) Read Only
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

#Task object custom filters
class TaskFliter(filters.FilterSet):
    
    class Meta:
        model = Task
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

#Creates defalt views for Task object
class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, 
    update and destroy actions
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


##
# This class extends Product filtering to include lte and gte for created timestamp. 
# Pretty much just testing - for use with transactions 
# to get the transactions from a certain date
class ProductFilter(filters.FilterSet):

    
    class Meta:
        model = Product
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

#Creates default views for Product objects
class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides list, create, retrieve, 
    update and destroy actions
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    __basic_fields = ('sku', 'name', 'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = ProductFilter

#Custom filter for brands
class BrandFilter(filters.FilterSet):

    class Meta:
        model = Brand
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

#Creates views for Brands
class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    __basic_fields = ('name', 'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = BrandFilter

#Custom filter for Suppliers
class SupplierFilter(filters.FilterSet):

    class Meta:
        model = Supplier
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

#Creates views for Suppliers
class SupplierViewSet(viewsets.ModelViewSet):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    __basic_fields = ('name', 'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = SupplierFilter


#Custom filter for departments
class DepartmentFilter(filters.FilterSet):

    class Meta:
        model = Department
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }


#Creates views for Departments
class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    __basic_fields = ('name', 'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = DepartmentFilter

#Custom filter for customers
class CustomerFilter(filters.FilterSet):

    class Meta:
        model = Customer
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

#Creates views for Customers
class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    __basic_fields = ('firstname', 'surname', 'id',  'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = CustomerFilter


#Custom filter for Transactions
class TransactionFilter(filters.FilterSet):

    class Meta:
        model = Transaction
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

#Creates views for Transactions
class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    __basic_fields = ('id', 'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = TransactionFilter

#Custom filter for productImage
class ProductImageFilter(filters.FilterSet):

    class Meta:
        model = ProductImage
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
        
    }

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    __basic_fields = ('imageName', 'created')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    filter_class = ProductImageFilter