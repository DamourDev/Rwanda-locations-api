import json
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Province, District, Sector, Cell, Village
from .serializers import ProvinceSerializer, DistrictSerializer, SectorSerializer, CellSerializer, VillageSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()  
    serializer_class = ProvinceSerializer  


class DistrictViewset(viewsets.ModelViewSet):
    queryset = District.objects.all()  
    serializer_class = DistrictSerializer


class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()  
    serializer_class = SectorSerializer  


class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()  
    serializer_class = CellSerializer  


class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()  
    serializer_class = VillageSerializer 