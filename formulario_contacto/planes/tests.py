
# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from planes.models import registro_cliente,nuevos_plan

class planesTestCase(TestCase):
        def setUp(self):
            userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
            )

class registroClienteTestCase(TestCase):
    def setUp(self):
        registro_cliente.objects.create(nombre='Ian',apellidoP="Garcia")
        registro_cliente.objects.create(nombre='Ricardo',apellidoP="Velozo")     

    def test_campos_cliente_correctos(self):
        obj1 = registro_cliente.objects.get(nombre='Ian')
        obj2 = registro_cliente.objects.get(nombre='Ricardo')
        self.assertEqual(obj1.nombre,'Ian')
        self.assertEqual(obj2.nombre,'Ricardo')
        self.assertEqual(obj1.apellidoP,'Velozo')
        self.assertEqual(obj2.apellidoP,'Sepulveda')
"""
class registroPlanTestCase(TestCase):
    def setUp1(self):
        nuevos_plan.objects.create(nombre_plan='Hogar',precio_plan=22900)
        nuevos_plan.objects.create(nombre_plan='Movil',precio_plan=19900)     

    def test_campos_plan_correctos(self):
        obj3 = nuevos_plan.objects.get(nombre_plan='Hogar')
        obj4 = nuevos_plan.objects.get(nombre_plan='Movil')
        self.assertEqual(obj3.nombre_plan,'Hogar')
        self.assertEqual(obj4.nombre_plan,'Movil')
        self.assertEqual(obj3.precio_plan,22©900)
        self.assertEqual(obj4.precio_plan,19900)   """  