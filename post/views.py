from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.viewsets import ModelViewSet
import django_filters
from post.filters import PostModelFilter
from .serializers import PostSerializer
from .models import Post
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class StandartResultPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter,django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category',]
    pagination_class = StandartResultPagination
    filter_class = PostModelFilter


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset







# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     lookup_field = 'id'
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
    

# написать FullCRUD на ModelViewSet(Post)
# n+1 & lazy queryset
# mixins | generics
# написать логику поиска и филтрации для постов