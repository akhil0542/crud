from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet
# from enroll.api import views
from . import views

router = DefaultRouter()
router.register('crud', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
