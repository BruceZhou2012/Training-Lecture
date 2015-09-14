from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.models import *
from restapi.serializers import SnippetSerializer
from rest_framework import generics
from django.http import Http404

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class SnippetList(generics.ListAPIView):

    serializer_class = SnippetSerializer

    def get_queryset(self):
        queryset = Snippet.objects.all()
        code = self.request.query_params.get('code', None)
        if code is not None:
            queryset = [ queryset.filter(code=code).values('id').last() ]
            print queryset
        else:
            raise Http404
            #print 1111
            #content = {'please move along': 'nothing to see here'}
            #return Response(content, status=status.HTTP_404_NOT_FOUND)
        return queryset
