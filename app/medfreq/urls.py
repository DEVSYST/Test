from django.conf.urls import url
from spyne.server.django import DjangoView

from .views import  app

from spyne.protocol.soap import Soap11

from.views import XmlService, JsonService

urlpatterns = [


    url(r'^xml/GetAllData', XmlService.get_xml, name='xml'),
    url(r'^json/GetAllData', JsonService.get_json, name='json'),
    url(r'^wsdl/', DjangoView.as_view(application=app)),

]
