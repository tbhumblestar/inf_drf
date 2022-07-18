from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .views import PostViewSet ,public_post_list

router = DefaultRouter()
router.register('post',PostViewSet)

urlpatterns = [
    # path('public/',public_post_list),
    path('',include(router.urls)),
]
