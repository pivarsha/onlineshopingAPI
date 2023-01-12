from rest_framework import serializers
from .models import Category,Product,Book,Cart
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=4)
    username = serializers.CharField(max_length=50,min_length=4)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password"
        )

    def validate(self, args):
        email = args.get("email",None)
        username = args.get("username",None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email":("email already exists")})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username":("username already exists")})

        return super().validate(args) 

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
            

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        
        model = Category


#Object Relational Mapping


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'image',
            'status',
            'date_created'
        )

        model = Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'image',
            'status',
            'date_created'
        )

        model = Product


class UserSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True,queryset=Book.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "books",
            "product"
        )


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True,many=False)
    books = BookSerializer(read_only=True,many=True)
    products = ProductSerializer(read_only=True,many=True)


    class Meta:
        model = Cart
        fields = (
            "cart_id",
            "created_at",
            "books",
            "products"
        )

