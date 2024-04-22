from rest_framework import serializers
from rest_framework.authtoken.models import Token
from sistema_informacion_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class AlumnoSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Alumnos
        fields = "__all__"
        
class AdminSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Administradores
        fields = '__all__'

class MaestroSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Maestros
        fields = '__all__'
#este apartado no es necesario ya que se puede 
#hacer con el modelo de usuario y estamos usando roles
class ProfilesAllSerializerAlumnos(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Alumnos
        fields = '__all__'
        depth = 1


# Clase para serializar las materias, es decir convertir los objetos en JSON
class MateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = '__all__'

# Clase para serializar las materias, es decir convertir los objetos en JSON, con mas detalle
class MateriasDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = '__all__'
        depth = 1
