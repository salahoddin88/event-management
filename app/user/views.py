from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for users  """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
