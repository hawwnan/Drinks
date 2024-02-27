# process of going from a python object to JSON 
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        # meta data describing the model
        model = Drink
        fields = ['id', 'name', 'description']
        #so we are going to use this when we are trying
        #to return our model through API
