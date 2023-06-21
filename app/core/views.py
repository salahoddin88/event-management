"""
Core views for app.
"""
from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheck(APIView):
    def get(self, request):
        """Returns successful response."""
        return Response({'healthy': True})
