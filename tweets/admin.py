from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'payload', 'like_count', 'created_at')

    def like_count(self, obj):
        return obj.likes.count()

    like_count.short_description = 'Likes'
