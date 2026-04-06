from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Check email to verify account"})
    
    return Response(serializer.errors)

@api_view(['GET'])
def verify_email(request, uid, token):
    try:
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Account verified"})
        
        return Response({"error": "Invalid token"})
    
    except User.DoesNotExist:
        return Response({"error": "User not found"})

@api_view(['GET'])
@ensure_csrf_cookie
def csrf_token(request):
    return Response({"csrfToken": get_token(request)})

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Logged in"})
    
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out"})

@api_view(['GET'])
def get_me(request):
    if request.user.is_authenticated:
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "is_authenticated": True,
        })
    
    return Response({"is_authenticated": False}, status=401)

@api_view(['POST'])
def password_reset(request):
    email = request.data.get('email')

    try:
        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)

        print(f"RESET LINK: /reset/{user.id}/{token}/")

        return Response({"message": "Reset email sent"})
    
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['POST'])
def password_reset_confirm(request):
    uid = request.data.get('uid')
    token = request.data.get('token')
    new_password = request.data.get('new_password')

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    if default_token_generator.check_token(user, token):
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password reset successful"})
    
    return Response({"error": "Invalid token"}, status=400)
    