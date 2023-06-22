from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import (
    views,
    authentication,
    permissions,
    response,
    status,
)


class LoginAPIView(ObtainAuthToken):
    """ Create a new auth token for users  """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LogoutAPIView(views.APIView):
    """ Delete a auth token of user """
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request):
        request.user.auth_token.delete()
        return response.Response(status=status.HTTP_200_OK)
