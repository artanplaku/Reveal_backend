# from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
# from django.contrib.auth import get_user_model CustomUser = get_user_model()


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format="json"):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomUserGet(APIView):

#     def get_user(self, username):
#         try:
#             return CustomUser.objects.get(username=username)
#         except CustomUser.DoesNotExist:
#             raise Http404

#     def get(self, request, format='json'):
#         user = self.get_user(request.user.username)
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)



class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class UsersList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer