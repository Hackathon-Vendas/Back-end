from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from heiwa.views import OrderViewSet, MPagoViewSet, UserViewSet, MesaViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Definindo o roteador
router = DefaultRouter()
router.register(r'orders', OrderViewSet)  # Corrigido para 'orders' no plural
router.register(r'users', UserViewSet)  # Corrigido para 'users' no plural
router.register(r'mesas', MesaViewSet)  # Corrigido para 'mesas' no plural

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mercadop/redirect',  MPagoViewSet.as_view({'get': 'redirect'}), name='homepage'),
    path('mercadop/homepage/', MPagoViewSet.as_view({'get': 'homepage'}), name='homepage'),
    path('mercadop/compracerta/', MPagoViewSet.as_view({'get': 'compracerta'}), name='compracerta'),
    path('mercadop/compraerrada/', MPagoViewSet.as_view({'get': 'compraerrada'}), name='compraerrada'),
]

