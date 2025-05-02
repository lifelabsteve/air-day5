from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tweet

class TweetAPITestCase(TestCase):
    def setUp(self):
        # 테스트용 사용자 생성
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = APIClient()
        # X-USERNAME 헤더 설정
        self.client.credentials(HTTP_X_USERNAME='testuser')
        
        # 테스트용 트윗 생성
        self.tweet = Tweet.objects.create(
            payload='테스트 트윗',
            user=self.user
        )

    def test_get_tweets(self):
        """GET /api/v1/tweets/ 테스트"""
        response = self.client.get('/api/v1/tweets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['payload'], '테스트 트윗')

    def test_create_tweet(self):
        """POST /api/v1/tweets/ 테스트"""
        data = {'payload': '새로운 트윗'}
        response = self.client.post('/api/v1/tweets/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 2)
        self.assertEqual(Tweet.objects.last().payload, '새로운 트윗')

    def test_get_tweet_detail(self):
        """GET /api/v1/tweets/<int:pk>/ 테스트"""
        response = self.client.get(f'/api/v1/tweets/{self.tweet.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payload'], '테스트 트윗')

    def test_update_tweet(self):
        """PUT /api/v1/tweets/<int:pk>/ 테스트"""
        data = {'payload': '수정된 트윗'}
        response = self.client.put(f'/api/v1/tweets/{self.tweet.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tweet.refresh_from_db()
        self.assertEqual(self.tweet.payload, '수정된 트윗')

    def test_delete_tweet(self):
        """DELETE /api/v1/tweets/<int:pk>/ 테스트"""
        response = self.client.delete(f'/api/v1/tweets/{self.tweet.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tweet.objects.count(), 0)

    def test_unauthorized_access(self):
        """인증되지 않은 접근 테스트"""
        self.client.credentials()  # 헤더 제거
        response = self.client.get('/api/v1/tweets/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
