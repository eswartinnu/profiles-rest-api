from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing APIView"""

    name = serializers.CharField(max_length=20)