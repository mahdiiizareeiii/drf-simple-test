from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from backend.models import Article
from .serializers import ArticleSerializer, UserSerializer
from .permissions import (
	IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
)

# Create your views here.
class ArticleViewSet(ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filterset_fields = ["status", "author"]
	ordering_fields = ["publish", "status"]
	ordering = ["-publish"]
	search_fields = [
		"title",
		"content",
		"author__username",
		"author__first_name",
		"author__last_name"
	]


	def get_permissions(self):
		if self.action in ['list', 'create']:
			permission_classes = [IsStaffOrReadOnly]
		else:
			permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
		return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly,)