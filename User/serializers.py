import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=100, default=None)
	password = serializers.CharField(default=None, max_length=255)
	profile_description = serializers.CharField(default='', max_length=2000)
	username = serializers.CharField(max_length=100, read_only=True)
	profile_pic = serializers.ImageField(default='profile_pics/default_pic.gif', read_only=True)
	is_staff = serializers.BooleanField(default=False, read_only=True)
	is_superuser = serializers.BooleanField(default=False, read_only=True)
	is_active = serializers.BooleanField(default = True, read_only=True)
	id = serializers.IntegerField(read_only=True)

	def create(self, validated_data) :
		return User.objects.create_user(**validated_data)