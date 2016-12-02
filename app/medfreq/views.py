from _mysql import IntegrityError

from django.http import HttpResponse
from medfreq.models import IllnessManager, IllnessItem
from spyne import Application, ResourceAlreadyExistsError, ResourceNotFoundError, rpc
from spyne.model.complex import Iterable
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.util.django import DjangoComplexModel, DjangoServiceBase, ValidationError

m = IllnessManager()


class Container(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = IllnessItem


class ContainerService(ServiceBase):
    @rpc(Integer, _returns=Container)
    def get_container(ctx, pk):
        try:
            return IllnessItem.objects.get(pk=pk)
        except IllnessItem.DoesNotExist:
            raise ResourceNotFoundError('Frequency')

    @rpc(Container, _returns=Container)
    def create_container(ctx, container):
        try:
            return IllnessItem.objects.create(**container.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError('Frequency')


class ExceptionHandlingService(DjangoServiceBase):
    """Service for testing exception handling."""

    @rpc(_returns=Container)
    def raise_does_not_exist(ctx):
        return IllnessItem.objects.get(pk=-1)

    @rpc(_returns=Container)
    def raise_validation_error(ctx):
        raise ValidationError('Is not valid.')


class XmlService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def get_xml(self):
        xml = m.read_xml()
        return HttpResponse(xml)


class JsonService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def get_json(self):
        jsn = m.read_json()
        return HttpResponse(jsn)


app = Application([ContainerService, ExceptionHandlingService, XmlService, JsonService],
                  'spyne.examples.django',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11(),
                  )
