from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'category')


class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

