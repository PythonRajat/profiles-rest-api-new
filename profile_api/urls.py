from django.urls import path, include
from profile_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view(), name='hello-view'),
    path('', include(router.urls))
]
