from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.company = None

        if request.user.is_authenticated and hasattr(request.user, 'company'):
            if hasattr(request.user, 'company'):
                request.company = request.user.company

        response = self.get_response(request)
        return response