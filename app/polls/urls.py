from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls import views


router = DefaultRouter()
router.register('polls', views.PollViewSet)

app_name = 'polls'

urlpatterns = [
    path('', include(router.urls))
]
