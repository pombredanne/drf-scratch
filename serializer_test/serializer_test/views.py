# -*- mode: python; coding: utf-8; -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .response import APIResponse
from .serializers import ResponseSerializer, User2Serializer


class SampleView(APIView):
    serializer_class = ResponseSerializer

    def get(self, request):
        user = User('dlesnov', 'dlesnov@iponweb.net')
        response = APIResponse()
        response.add_object(user)
        # response.set_error('23423')
        serializer = self.serializer_class(response)
        return Response(serializer.data)

sample_view = SampleView.as_view()


class SampleView2(APIView):
    def get(self, request):
        User = get_user_model()
        user = User(id=1, username='ifedorov', email='ifedorov@iponweb.net')
        return Response(User2Serializer(user).data)

sample_view_2 = SampleView2.as_view()
