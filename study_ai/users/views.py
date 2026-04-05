from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
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
    from django.contrib.auth import authenticate, login

@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return Response({"message": "Logged in"})
    
    return Response({"error": "Invalid credentials"})
from django.contrib.auth import logout

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out"})
@api_view(['GET'])
def get_me(request):
    if request.user.is_authenticated:
        return Response({
            "id": request.user.id,
            "username": request.user.username
        })
    
    return Response({"error": "Not logged in"})
@api_view(['POST'])
def password_reset(request):
    email = request.data['email']

    try:
        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)

        print(f"RESET LINK: /reset/{user.id}/{token}/")

        return Response({"message": "Reset email sent"})
    
    except User.DoesNotExist:
        return Response({"error": "User not found"})
@api_view(['POST'])
def password_reset_confirm(request):
    uid = request.data['uid']
    token = request.data['token']
    new_password = request.data['new_password']

    user = User.objects.get(pk=uid)

    if default_token_generator.check_token(user, token):
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password reset successful"})
    
    return Response({"error": "Invalid token"})
    