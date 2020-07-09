from .models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    mentor = serializers.StringRelatedField()
    class Meta:
        model = Quiz
        fields = '__all__'
