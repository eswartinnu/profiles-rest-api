from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        api_view = [
            'Uses HTTP Methods as funtions (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives complete control over the application logic',
            'Is mapped manuallt to URLs'
        ]

        return Response({'message': 'Hello!', 'api_view': api_view})
