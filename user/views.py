from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from .utils import unhash_token
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound, AuthenticationFailed
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser



class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()


            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "uid": user.uid,
                "message": "User registered successfully!",
                "refresh": str(refresh),
                "access": access_token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RetrieveProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uid'

    def get(self, request, *args, **kwargs):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')

        if not user_id:
            raise NotFound("User not found")

        user = get_object_or_404(User, uid=user_id)
        serializer = self.get_serializer(user)

        return Response(serializer.data)



class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user



class DeleteProfileAPIView(generics.DestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uid'

    def get_queryset(self):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')
        return User.objects.filter(uid=user_id)

    def perform_destroy(self, instance):

        instance.delete()

    def delete(self, request, *args, **kwargs):

        user = self.get_object()

        self.perform_destroy(user)

        return Response({"message": "User successfully deleted"}, status=status.HTTP_204_NO_CONTENT)





