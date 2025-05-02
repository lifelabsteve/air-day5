from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get('X-USERNAME')
        
        if not username:
            return None  # 인증 실패 시 None 반환
            
        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            return None  # 인증 실패 시 None 반환

    def authenticate_header(self, request):
        return 'X-USERNAME'  # WWW-Authenticate 헤더 설정 