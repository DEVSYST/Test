from django.conf.urls import url
from spyne.server.django import DjangoView

from .views import app, XmlService, JsonService

urlpatterns = [
    url(r'^xml/GetAllData', XmlService.get_xml, name='xml'),
    url(r'^json/GetAllData', JsonService.get_json, name='json'),
    url(r'^wsdl', DjangoView.as_view(application=app)),
]
