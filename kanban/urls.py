from rest_framework_nested import routers
from .views import ProjectViewSet, TicketViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='project')

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'tickets', TicketViewSet, basename='project-tickets')

urlpatterns = [
        path(r'', include(router.urls)),
        path(r'', include(projects_router.urls)),
        ]
