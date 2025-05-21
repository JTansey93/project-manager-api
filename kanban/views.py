from django.shortcuts import get_object_or_404
from .serializers import ProjectSerializer, TicketSerializer
from .models import Project, Ticket
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_pk'])
        serializer.save(project=project)

                                    

