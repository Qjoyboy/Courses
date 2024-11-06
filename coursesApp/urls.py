from django.urls import path

from coursesApp.apps import CoursesappConfig
from coursesApp.views.course import CourseViewSet
from rest_framework.routers import DefaultRouter

from coursesApp.views.course import *
from coursesApp.views.lesson import *

app_name = CoursesappConfig.name

router = DefaultRouter()
router.register(r'coursesApp', CourseViewSet, basename='coursesApp')

urlpatterns = [
    path('', LessonListView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('<int:pk>/update', LessonUpdateView.as_view()),
    path('<int:pk>/delete', LessonDeleteView.as_view()),
] + router.urls