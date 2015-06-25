# -*- mode: python; coding: utf-8; -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rest_framework import serializers

from .models import User


class ResponseMetaSerializer(serializers.Serializer):
    pass


class ResponseDataSerializer(serializers.DictField):
    # @property
    # def child(self):
    #     return ResponseDataSerializer()

    def wrap_models_to_serializers(self, data):
        if isinstance(data, dict):
            return {
                k: self.wrap_models_to_serializers(v)
                for k, v in data.items()
            }

        if data.__class__ in model_serializers:
            return model_serializers[data.__class__](data).data

        return data

    def to_representation(self, value):
        print('*'*80, value)
        wrapped = self.wrap_models_to_serializers(value)
        print('*'*80, wrapped)

        return super(ResponseDataSerializer, self).to_representation(wrapped)


class UserSerializer(serializers.Serializer):
    uid = serializers.CharField()
    email = serializers.EmailField()


class ResponseSerializer(serializers.Serializer):
    meta = ResponseMetaSerializer()
    error = serializers.CharField(required=False)
    data = ResponseDataSerializer()
    # data = serializers.DictField()


class User2Serializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()



model_serializers = {
    User: UserSerializer
}
