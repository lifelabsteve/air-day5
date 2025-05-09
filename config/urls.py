"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweets.views import (
    TweetListCreateAPIView,
    TweetRetrieveUpdateDestroyAPIView,
    UserListCreateAPIView,
    UserRetrieveAPIView,
    UserTweetListAPIView,
    ChangePasswordAPIView,
    LoginAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tweets/', TweetListCreateAPIView.as_view(), name='tweet-list-create'),
    path('api/v1/tweets/<int:pk>/', TweetRetrieveUpdateDestroyAPIView.as_view(), name='tweet-detail'),
    path('api/v1/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/v1/users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('api/v1/users/<int:pk>/tweets/', UserTweetListAPIView.as_view(), name='user-tweet-list'),
    path('api/v1/users/password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('api/v1/users/login/', LoginAPIView.as_view(), name='login'),
    path('api/v1/users/logout/', LogoutAPIView.as_view(), name='logout'),
]