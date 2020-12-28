from rest_framework import serializers

class ContactSerializer(serializers.ModelSrializers):
    class meta:
        class Meta:
            model=Contact
            fields='__all__'
