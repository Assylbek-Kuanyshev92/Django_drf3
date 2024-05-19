from django import forms
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = ['title', 'content', 'demo_content']

# class CommentSerializer(serializers.ModelSerializer):
#
#         class Meta:
#             model = Comment
#             fields = ['title']