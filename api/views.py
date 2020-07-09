from .models import Quiz
from rest_framework import viewsets, permissions
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quizes to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    queryset = Quiz.objects.all().order_by('-createdOn')
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        serializer.save(mentor=self.request.user)