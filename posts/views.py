from rest_framework import generics
from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import isAuthorOrReadOnly
class PostList(generics.ListCreateAPIView):
    permission_classes = (isAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
