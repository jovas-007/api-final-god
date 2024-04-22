from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from sistema_informacion_api.serializers import *
from sistema_informacion_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json


# Metodo para obtener todas las materias
class MateriasAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
# Este metodo retorna todas las materias

    def get(self, request, *args, **kwargs):
        materias = Materias.objects.all().order_by("id")
        lista = MateriasSerializer(materias, many=True).data

        return Response(lista, 200)


# Metodo para obtener una materia por ID
class MateriasView(generics.CreateAPIView):
    # Obtener materia por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, id=request.GET.get("id"))
        materia_data = MateriasSerializer(materia, many=False).data

        return Response(materia_data, 200)

    # Registrar nueva materia
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Grabar datos de la materia
        materia = MateriasSerializer(data=request.data)
        if materia.is_valid():
            materia.save()
            return Response({"materia_created_id": materia.data["id"]}, 201)
        return Response(materia.errors, status=status.HTTP_400_BAD_REQUEST)

# Metodo para editar y eliminar una materia


class MateriasViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        # Esto ayuda a obtener el objeto que se va a editar a traves del id(id=request.data["id"])
        materia = get_object_or_404(Materias, NRC=request.data["NRC"])
        materia.nombre = request.data["nombre"]
        materia.seccion = request.data["seccion"]
        materia.dias = request.data["dias"]
        materia.horaInicio = request.data["horaInicio"]
        materia.horaFinal = request.data["horaFinal"]
        materia.salon = request.data["salon"]
        materia.programaEducativo = request.data["programaEducativo"]
        materia.save()
        mat = MateriasSerializer(materia, many=False).data

# Este metodo retorna la materia editada
        return Response(mat, 200)


# Metodo para eliminar una materia


    def delete(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, id=request.GET.get("id"))
        try:
            materia.delete()
            return Response({"details": "Materia eliminada"}, 200)
        except Exception as e:
            return Response({"details": "Algo pasó al eliminar"}, 400)
