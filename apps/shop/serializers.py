from rest_framework import serializers

from .models import (
    Category,
    Product,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class ProductCountSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_count = serializers.IntegerField()

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if attrs['product_count'] < 0:
            raise serializers.ValidationError(
                'product_count must not be >= 0'
            )

        if not Product.objects.filter(id=attrs['product_id']).exists():
            raise serializers.ValidationError(
                f"Product id={attrs['product_id']} does not exist"
            )

        return attrs
