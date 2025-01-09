from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, RegisterViewSet, AllproductListViewSet
router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('register', RegisterViewSet, basename='register')
router.register('allproducts', AllproductListViewSet, basename='allproduct')

urlpatterns = [
    path('', include(router.urls)),
]
