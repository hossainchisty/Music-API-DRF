from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

routes = DefaultRouter()

routes.register('singer', views.SingerViewSet, basename='singer')
routes.register('song', views.SongViewSet, basename='song')

urlpatterns = [
    path('', include(routes.urls)),
]
