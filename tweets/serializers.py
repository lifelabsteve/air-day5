from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Tweet

class TweetSerializer:
    def serialize(self, queryset):
        data = []
        for tweet in queryset:
            data.append({
                'id': tweet.id,
                'payload': tweet.payload,
                'user': tweet.user.id,
                'created_at': tweet.created_at.isoformat(),
                'updated_at': tweet.updated_at.isoformat()
            })
        return data