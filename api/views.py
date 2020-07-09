from .models import Quiz
from rest_framework import viewsets
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quizes to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer