from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
import uuid
from rest_framework import status,permissions



# Create your views here.

class RegistrationAPIViews(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"RequestId":str(uuid.uuid4()),
            "Message":"User Created Successfully",
            "User":serializer.data},status=status.HTTP_201_CREATED) 
        return Response({"Errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListBook(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class  = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class=CartSerializer

def form(request):
    return render(request,"form.html")