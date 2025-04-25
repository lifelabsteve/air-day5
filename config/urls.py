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
from tweets.views import tweet_list, TweetListAPIView, UserTweetListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweet_list, name='tweet_list'),  # 메인 페이지에 트윗 목록 표시
    path('api/v1/tweets/', TweetListAPIView.as_view(), name='api_tweet_list'),
    path('api/v1/users/<int:user_id>/tweets/', UserTweetListAPIView.as_view(), name='api_user_tweet_list'),
]