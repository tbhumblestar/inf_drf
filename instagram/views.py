
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework.decorators import action
from .models import Post

from instagram.serializers import PostSerializer

#CBV ver Listview
class PublicPostListAPIView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

#FBV ver Listview
class PublicPostListAPIView(APIView):
  def get(self,request,format=None):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs,many=True)
    return Response(serializer.data)

public_post_list = PublicPostListAPIView.as_view() 

class PostViewSet(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  @action(detail=False,methods=['GET'])
  def public(self,request):
    qs = self.get_queryset().filter(is_public=True)
    serializer = self.get_serializer(qs,many=True)
    return Response(serializer.data)
  
  @action(detail=True,methods=['PATCH'])
  def set_public(self,request,pk):
    instance = self.get_object()
    instance.is_public = True

    instance.save()
    #이렇게도 할 수 있음. 근데 어차피 수정된 필드가 하나밖에 없어서, 결과가 같긴함. 대신 db에부담이 덜하것쥬
    #instance.save(update_fields = ['is_public]'])

    #이런 메서드에서 클래스변수로 설정해준 serializer를 들고올때 get_serializer를 많이 사용함
    serializer = self.get_serializer(instance)
    return Response(serializer.data)
