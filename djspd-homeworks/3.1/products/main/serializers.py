from rest_framework import serializers
from .models import Review
from .models import Product
class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = "__all__"
        # реализуйте все поля



class ProductListSerializer(serializers.Serializer):
      class Meta:
            model = Product
            fields = ["title","price"]



class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title","description", "price","reviews"]
        # реализуйте поля title, description, price и reviews (список отзывов к товару)

