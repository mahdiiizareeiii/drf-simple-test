from rest_framework import serializers
from backend.models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ("title", "slug", "author", "content", "publish", "status")
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        #fields = ("title", "slug", "author", "content", "publish", "status")
        fields = "__all__"