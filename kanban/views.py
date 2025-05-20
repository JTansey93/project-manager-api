from django.shortcuts import get_object_or_404
from .serializers import ProjectSerializer, TicketSerializer
from .models import Project, Ticket
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class ProjectViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)


