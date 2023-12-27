from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.viewsets import ModelViewSet
import django_filters
from post.filters import PostModelFilter
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .permissions import IsStuff, IsOwner



class StandartResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated, IsStuff]
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['content']
    filterset_fields = ['post']
    # filterset_class = PostModelFilter


    def get(self, request, *args, **kwargs):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.AllowAny()]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

