import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response

from django.contrib.auth.models import User
from api.permissions import IsAccountOwner, IsAuthorOfPost
from api.serializers import AccountSerializer, PostSerializer

from api.models import Post



class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    print queryset
    serializer_class = AccountSerializer
    #print "AccountSerializer mein aaa gaya", viewsets.ModelViewSet
    def get_permissions(self):
        #print "permissions mein aaa gaya", self.request.method, permissions.SAFE_METHODS
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            #print "In Post"
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        print "create mein aaa gaya", self.serializer_class(data=request.data)," ji"
        serializer = self.serializer_class(data=request.data)
        print request.data
        if serializer.is_valid():
            print "users mein aa gaya"
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        print request.data
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        print "In Login"
        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)



###############################################################
# Post Specific Views
###############################################################

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(PostViewSet, self).perform_create(serializer)


class AccountPostsViewSet(viewsets.ViewSet):
    queryset = Post.objects.select_related('author').order_by('-created_at')
    serializer_class = PostSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

