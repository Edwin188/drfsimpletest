from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
