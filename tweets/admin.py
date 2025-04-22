from django.contrib import admin
from .models import Tweet,Like

# Custom Filter for "Elon Musk" 포함 여부
class ElonMuskFilter(admin.SimpleListFilter):
    title = 'Elon Musk 포함 여부'
    parameter_name = 'elon_musk'

    def lookups(self, request, model_admin):
        return (
            ('contains', 'Elon Musk 포함'),
            ('not_contains', 'Elon Musk 미포함'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'contains':
            return queryset.filter(payload__icontains='elon musk')
        elif self.value() == 'not_contains':
            return queryset.exclude(payload__icontains='elon musk')
        return queryset

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'payload', 'like_count', 'created_at')
    search_fields = ('payload', 'user__username')  # payload 및 사용자명으로 검색
    list_filter = ('created_at', ElonMuskFilter)   # 생성일 및 커스텀 필터

    def like_count(self, obj):
        return obj.likes.count()

    like_count.short_description = 'Likes'

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'tweet', 'user', 'created_at')
    search_fields = ('user__username',)        # 사용자명으로 검색
    list_filter = ('created_at',)              # 생성일 필터