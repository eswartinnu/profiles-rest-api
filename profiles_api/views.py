from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        api_view = [
            'Uses HTTP Methods as funtions (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives complete control over the application logic',
            'Is mapped manuallt to URLs'
        ]

        return Response({'message': 'Hello!', 'api_view': api_view})

    def post(self, request, format=None):
        """Create a hello Message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk= None):
        """Handle updating objects"""
        return Response({'Method':'put'})
    
    def patch(self, request, pk= None):
        """Handle partial update of objects"""
        return Response({'Method':'patch'})
    
    def delete(self, request, pk= None):
        """Delete of objects"""
        return Response({'Method':'Delete'})
    
