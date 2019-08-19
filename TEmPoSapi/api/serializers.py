from rest_framework import serializers
from api.models import CustomUser, Product, Brand, Customer, Transaction, ProductImage, Supplier, Department, Task

##THIS IS THE NEWER VERSION THAT USES URLS

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Task
        fields = ('url', 'id', 'created', 'user', 'title', 'description', 'status')

#Serializer for Custom User object
class UserSerializer(serializers.HyperlinkedModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)
    #tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'id',  'username', 'profilePicture', 'tasks')



class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ('url', 'id', 'created', 'product', 'imageName', 'image')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Department
        fields = ('id', 'url', 'name')


#Serializer for Product objects
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    brand = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Brand.objects.all(),
        allow_null=True,
    )
    
    department = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Department.objects.all(),
        allow_null=False,
    )

    productImages = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('url', 'id', 'created', 'name', 'sku', 'brand', 'mainImage', 'productImages', 'department')



#Serializer for Brand objects
class BrandSerializer(serializers.HyperlinkedModelSerializer):

    supplier = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Supplier.objects.all(),
        allow_null=True,
    )



    class Meta:
        model = Brand
        fields = ('url','id','created','name', 'supplier')

#Serializer for Supplier objects
class SupplierSerializer(serializers.HyperlinkedModelSerializer):

    brands = BrandSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ('url','id','created','name', 'brands')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('url', 'id','created', 'firstname', 'surname')

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('url','id','created', 'customer', 'product')

