from rest_framework import serializers
from .models import Shop, Item, ItemImage

class ShopSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shop
    fields = '__all__'
    
# class ItemSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Item
#     fields = '__all__'


class ItemImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ItemImage
        fields = ['image']


class ItemSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.itemimage_set.all()
        return ItemImageSerializer(instance=image, many=True).data

    class Meta:
        model = Item
        fields = ['id', 'name', 'type', 'images']
        
        
    def create(self, validated_data):
        instance = Item.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            ItemImage.objects.create(item=instance, image=image_data)
        return instance