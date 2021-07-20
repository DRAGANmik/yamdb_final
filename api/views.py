from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import TitleFilter
from .models import Category, Comment, Genre, Review, Title
from .permissions import IsAdmin, IsModeratorOrAuthor
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    TitleReadSerializer,
    TitleWriteSerializer,
)


class CreateListDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg("reviews__score")).order_by(
        "rating"
    )
    serializer_class = TitleWriteSerializer
    permission_classes = [IsAdmin, IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        actions = ["list", "retrieve"]
        if self.action in actions:
            return TitleReadSerializer
        return TitleWriteSerializer


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [IsAdmin, IsAuthenticatedOrReadOnly]


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    lookup_field = "slug"
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [IsAdmin, IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsModeratorOrAuthor]

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title_id=self.kwargs.get("title_id"),
        )
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title_id=self.kwargs.get("title_id"),
        )
        return Comment.objects.filter(review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsModeratorOrAuthor]

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        return Review.objects.filter(title=title)
