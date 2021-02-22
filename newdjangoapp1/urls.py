from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from djangoapp import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from djangoapp.models import sample,post
from djangoapp.serializers import PostSerializer




class SamplesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sample
        fields = ['name', 'phone']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = sample.objects.all()
    serializer_class = SamplesSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class =PostSerializer 

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'post',PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('new/',include('djangoapp.urls'))
]
