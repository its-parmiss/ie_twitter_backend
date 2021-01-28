from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.db import models
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Account, UserFollowing, Like, Image
from .models import Tweet


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


# class TweetSerializer(serializers.ModelSerializer):
#     likes=LikeSerializer(read_only=True, many=True)
#     class Meta:
#         model = Tweet
#         fields=['id','text','user_id','date','likes']
class TweetSerializer(serializers.ModelSerializer):
    parent = RecursiveField(allow_null=True)

    class Meta:
        model = Tweet
        fields = ['id', 'text', 'user', 'date', 'likes', 'parent']


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'bio', 'birthdate')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = Account.objects.create_user(validated_data['username'], password=validated_data['password'],
                                           first_name=validated_data['first_name'],
                                           last_name=validated_data['last_name'], email=validated_data['email'])
        return user


class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ('user_id', 'following_user_id')


class UserSerializer(serializers.ModelSerializer):
    following = UserFollowingSerializer(read_only=True, many=True)
    followers = UserFollowingSerializer(read_only=True, many=True)
    tweets = TweetSerializer(read_only=True, many=True)
    liked = LikeSerializer(read_only=True, many=True)

    class Meta:
        model = Account
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]
