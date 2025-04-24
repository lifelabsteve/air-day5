from django.shortcuts import render
from django.http import JsonResponse
from .models import Tweet
from .serializers import TweetSerializer
from django.contrib.auth.models import User

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

def api_tweet_list(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer()
    data = serializer.serialize(tweets)
    return JsonResponse(data, safe=False)

def api_user_tweet_list(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer()
        data = serializer.serialize(tweets)
        return JsonResponse(data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({"error": "사용자를 찾을 수 없습니다."}, status=404)