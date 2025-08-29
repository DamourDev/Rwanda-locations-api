from django.urls import path, include
from rest_framework import routers
from .views import (
    ProvinceViewSet, DistrictViewset,
    SectorViewSet, CellViewSet, VillageViewSet
)

from . import views

# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'provinces', ProvinceViewSet)
router.register(r'districts', DistrictViewset)
router.register(r'sectors', SectorViewSet)
router.register(r'cells', CellViewSet)
router.register(r'villages', VillageViewSet)

# URLs from router will now be included
# urlpatterns = [
    # path('', views.Load_data),
    # path('home/', views.home, name="home"),
    # path('clear/', views.clear, name="clear")
# ]

urlpatterns = [
    path('', include(router.urls)),
]