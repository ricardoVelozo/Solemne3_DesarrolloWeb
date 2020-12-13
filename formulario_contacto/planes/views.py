from django.shortcuts import render
from rest_framework import viewsets
from planes.models import registro_cliente

from formulario_contacto.serializers import registroClienteSerializers

class registroClienteViewset(viewsets.ModelViewSet):
    queryset = registro_cliente.objects.all()
    serializer_class=registroClienteSerializers

