from django.shortcuts import render
from .models import Tweet

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # 최신 트윗이 먼저 보이도록 정렬
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})