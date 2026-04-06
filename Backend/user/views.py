from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

# REGISTER
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        token = default_token_generator.make_token(user)

        print(f"VERIFY LINK: /verify/{user.id}/{token}/")

        return Response({"message": "Check email to verify account"})

    return Response(serializer.errors, status=400)


# VERIFY EMAIL
@api_view(['GET'])
def verify_email(request, uid, token):

    try:
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()

            return Response({"message": "Account verified"})

        return Response({"error": "Invalid token"})

    except User.DoesNotExist:
        return Response({"error": "User not found"})


# LOGIN
@api_view(['POST'])
def login_view(request):

    user = authenticate(
        username=request.data.get('username'),
        password=request.data.get('password')
    )

    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    if not user.is_verified:
        return Response({"error": "Verify email first"}, status=403)

    login(request, user)

    return Response({"message": "Logged in"})


# LOGOUT
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out"})


# CURRENT USER
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):

    serializer = UserSerializer(request.user)

    return Response(serializer.data)


# PASSWORD RESET
@api_view(['POST'])
def password_reset(request):

    email = request.data.get('email')

    try:
        user = User.objects.get(email=email)

        token = default_token_generator.make_token(user)

        print(f"RESET LINK: /reset/{user.id}/{token}/")

    except User.DoesNotExist:
        pass

    return Response({"message": "If email exists, reset link sent"})


# PASSWORD RESET CONFIRM
@api_view(['POST'])
def password_reset_confirm(request):

    uid = request.data.get('uid')
    token = request.data.get('token')
    new_password = request.data.get('new_password')

    try:
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()

            return Response({"message": "Password reset successful"})

        return Response({"error": "Invalid token"})

    except User.DoesNotExist:
        return Response({"error": "User not found"})