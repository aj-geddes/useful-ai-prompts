# Authentication and Permissions

## Authentication and Permissions

```python
# users/views.py
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from rest_framework.authtoken.models import Token
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

@require_http_methods(['POST'])
@csrf_protect
def login_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({
            'success': True,
            'token': token.key,
            'user_id': user.id
        })

    return JsonResponse({'error': 'Invalid credentials'}, status=401)

@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True})
```
