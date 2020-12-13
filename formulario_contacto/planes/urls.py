from django.urls import path, include
from .models import Planes
from rest_framework import routers, serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

#Encargado de serializar los datos que llegan
class PlanesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planes
        fields = ['id','nombre', 'precio', 'fecha_inicio', 'fecha_termino']

class PlanesViewSet(viewsets.ModelViewSet):
    queryset = Planes.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    serializer_class = PlanesSerializer
    filterset_fields = ['id','nombre']
    search_fields = ['id','nombre']

router = routers.DefaultRouter()
router.register(r'', PlanesViewSet)

urlpatterns = [
    path('', include(router.urls))
]