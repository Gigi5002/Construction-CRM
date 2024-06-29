from rest_framework import viewsets
from .models import Apartment
from .serializers import ApartmentSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
