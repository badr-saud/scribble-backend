from rest_framework import generics, viewsets
from .serializers import NoteSerializer, TagSerializer
from .models import Note, Tag
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
