from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt import views as jwt_views
# from django.conf import settings
# from django.conf.urls.static import static


## For schema views
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='TEmPoS API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'productImages', views.ProductImageViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'tasks', views.TaskViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('schema/', schema_view)
] 
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)