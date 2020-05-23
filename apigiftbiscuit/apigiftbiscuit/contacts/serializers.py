from rest_framework import serializers
from .models import Contact

import re

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = (
            'name', 
            'email', 
            'phone', 
            'message'
        )

    def validate_name(self, value):
        regex =  "[a-zA-Z]+$"

        if not value is None:
            if re.search(regex, value):
                return value
        raise serializers.ValidationError('O valor deste campo é inválido.')

    def validate_phone(self, value):
        regex = "\(\d{2}\)\d{5}-\d{4}"

        if not value is None:
            if re.search(regex, value):
                return value
        raise serializers.ValidationError('O valor deste campo é inválido. Use o formato (99)99999-9999.')

    def validate_message(self, value):
        if not value is None:
            if len(value) >= 10:
                return value
        raise serializers.ValidationError('O valor deste campo é muito curto.')
