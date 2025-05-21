#TODO: Add serialisers for project, ticket and user models
from rest_framework import serializers
from .models import Project, Ticket

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['project', 'name', 'description', 'status', 'assignee']
