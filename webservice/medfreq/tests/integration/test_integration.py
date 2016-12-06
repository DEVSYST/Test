from django.test import TestCase
from spyne import Fault
from spyne.client.django import DjangoTestClient

from medfreq.views import app, IllnessItem

from suds.client import Client
from suds.cache import NoCache

from django.test import LiveServerTestCase

#from medfreq.models import IllnessItem


class WsdlTest(LiveServerTestCase):
    def setUp(self):
        self.longMessage = True

        client = Client('%s/medfreq/wsdl/' % self.live_server_url,
                        cache=NoCache(),
                        )
        self.client = client

    def test_disease(self):
        print dir(self.client)
        print self.client.wsdl
        disease = self.client.factory.create('JsonService')
        print "diss1: ", disease
        disease.name = "flu"
        disease.frequencies = [0.3, 0.6, 0.9]
        disease.duty_cycle = 40
       # print "diss2: ", disease
       # print dir(disease)
       # print dir(self.client.service)

        print "cont:", disease, type(disease)
        # ill = IllnessItem()
        # x1 = self.client.service.create_container(ill)
        # print "x1: ", x1


       # xml = self.client.service.get_container(1)
        #print "data: ", xml

