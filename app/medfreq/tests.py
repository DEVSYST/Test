from django.test import TestCase
from spyne import Fault
from spyne.client.django import DjangoTestClient

from medfreq.views import app, Container

from suds.client import Client
from suds.cache import NoCache

from django.test import LiveServerTestCase

from medfreq.models import IllnessItem


class WsdlTest(LiveServerTestCase):
    def setUp(self):
        self.longMessage = True

        client = Client('%s/medfreq/wsdl/' % self.live_server_url,
                        autoblend=True,
                        cache=NoCache(),
                        timeout=420,
                        )
        self.client = client

    def test_simple(self):
        disease = self.client.factory.create('IllnessItem')
        disease.name = ""
        disease.frequencies = []
        disease.duty_cycle = 40
