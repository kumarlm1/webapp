from django.contrib.auth.models import Group,User
from rest_framework import serializers
from djangoapp.models import sample,posts,post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields=['url','username','email','group']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']  

class SamplesSerializer(serializers.HyperlinkedModelSerializer):
    name=serializers.HyperlinkedRelatedField(many=True,view_name='user',read_only=True)
    owner=serializers.ReadOnlyField(source='owner.name')
    class Meta:
        model = sample
        fields=['id','url','name','phone']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model =  post 
        fields=['name','post_number','message']                  