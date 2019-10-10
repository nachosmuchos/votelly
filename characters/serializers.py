from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'description', 'image_alt_text', 
        'number_of_votes', 'related_program', 'character_photo')