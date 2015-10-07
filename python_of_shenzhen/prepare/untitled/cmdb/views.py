from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from cmdb.models import UpdateInfo
from cmdb.serialization import CMDBSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class CMDBViews(viewsets.ViewSet):
    def list(self, request):
        """

        http http://127.0.0.1:8000/api/data/

        :param request:
        :return:
        """
        model_object = UpdateInfo.objects.all()
        serializer = CMDBSerializer(model_object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        http http://127.0.0.1:8000/api/data/1/
        :param request:
        :param pk:
        :return:
        """
        model_object = UpdateInfo.objects.all()
        # model_object = model_object[1:9]

        # model_object = UpdateInfo.objects.all()[1:9]

        """
        Method(1)
        (1) . model_object = select * from UpdateInfo
        (2) . model_object limit 1 to 9

        Method(2)
        (1) . model_object = select * from UpdateInfo limit 1 to 9

        """

        queryset = get_object_or_404(model_object, pk=pk)

        serializer = CMDBSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """

        http POST  http://127.0.0.1:8000/api/data/ uuid='12345'

        :param request:
        :return:
        """
        serializer = CMDBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """

        http PUT  http://127.0.0.1:8000/api/data/1/ status='online'
        :param request:
        :param pk:
        :return:
        """

        model_object = UpdateInfo.objects.all()
        queryset = get_object_or_404(model_object, pk=pk)
        serializer = CMDBSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        """
        http DELETE  http://127.0.0.1:8000/api/data/4/

        :param request:
        :param pk:
        :return:
        """

        model_object = UpdateInfo.objects.all()
        queryset = get_object_or_404(model_object, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetList(generics.ListAPIView):
    serializer_class = CMDBSerializer

    def get_queryset(self):
        queryset = UpdateInfo.objects.all()
        # username = self.request.query_params.get('username', None)
        username = self.kwargs['username']
        uu = username.split('=')[1]
        print username
        return queryset.filter(id=uu)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CMDBSerializer(queryset, many=True)
        if not serializer.data:
            return Response('error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data, status=status.HTTP_200_OK)
