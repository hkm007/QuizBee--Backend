from django.contrib.auth.models import User
from .models import Quiz
from rest_framework import viewsets
from .serializers import UserSerializer, QuizSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quizes to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer