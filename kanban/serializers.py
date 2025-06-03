#TODO: Add serialisers for project, ticket and user models
from rest_framework import serializers
from .models import Project, Ticket

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        # The FE needs the pk to be able to distinguish between objects in the db
        model = Project
        fields = ['pk', 'name']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        # Same logic as project serializer for adding pk
        model = Ticket
        fields = ['pk', 'project', 'name', 'description', 'status', 'assignee']
