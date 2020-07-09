from django.contrib.auth.models import User
from .models import Quiz
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'mentor', 'createdOn', 'q1', 'a1', 'q2', 'a2', 'q3', 'a3', 'q4', 'a4', 'q5', 'a5', 'q6', 'a6', 'q7', 'a7', 'q8', 'a8', 'q9', 'a9', 'q10', 'a10']
