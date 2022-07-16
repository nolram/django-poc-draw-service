from datetime import datetime

from django.http import JsonResponse
from django.views.generic import View

class HealthCheck(View):

    def get(self, *args, **kwargs):
        response = JsonResponse(
            data={'date': datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'), "status": "OK"},
        )
        return response