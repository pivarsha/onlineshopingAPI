from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category,related_name="books",on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="static/books")
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=50) 
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="static/books")
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.product_tag} {self.name}"



class Cart(models.Model):
    cart_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    products = models.ManyToManyField(Product)


    class Meta:
        ordering = ["cart_id","-created_at"]

    def __str__(self):
        return f"{self.cart_id}"




