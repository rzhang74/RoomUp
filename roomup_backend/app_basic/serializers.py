from rest_framework import serializers

from app_basic.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class AdvancedUserSerializer(serializers.ModelSerializer):
    uid = UserSerializer(serializers.ModelSerializer, required=True)
    class Meta:
        model = AdvancedUser
        fields = ('uid', 'gid', 'gender', 'age', 'ethinicity', 'quietness', 'sanitary', \
                  'timetobed', 'pet', 'major', 'hobbies', 'language', 'graduationyear', \
                  'note')

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('aid', 'name',  'price', 'address', 'floorplan', 'occupied')

class GroupSerializer(serializers.ModelSerializer):
    admin_uid = AdvancedUserSerializer(serializers.ModelSerializer)
    aid = ApartmentSerializer(required=True)
    class Meta:
        model = Group
        fields = ('gid', 'group_name', 'capacity', 'aid', 'peopleleft', 'admin_uid', 'active')


class PotentialMatchSerializer(serializers.ModelSerializer):
    gid = GroupSerializer(required=True)
    uid = AdvancedUserSerializer(required=True)
    class Meta:
        model = PotentialMatch
        fields = ('pid', 'uid', 'gid')

class ChatSerializer(serializers.ModelSerializer):
    # TODO: make chat RESTful
    pass

