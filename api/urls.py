from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.api import OrderViewSet, ProductViewSet,MyTokenObtainPairView
from api import api



urlpatterns = [
    path("", api.getRoutes, name="getRoutes"),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = routers.DefaultRouter()
router.register('api/products', ProductViewSet, 'products')
router.register('api/orders', OrderViewSet, 'orders')

urlpatterns += router.urls