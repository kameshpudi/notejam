import os

from django.core.wsgi import get_wsgi_application

# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.
settings_module = "azuresite.production" if 'WEBSITE_HOSTNAME' in os.environ else 'notejam.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
