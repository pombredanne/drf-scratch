# -*- mode: python; coding: utf-8; -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import defaultdict


class APIResponse(object):
    def __init__(self):
        self.meta = {}
        self._error = None
        self.data = defaultdict(dict)

    def set_error(self, error_code):
        self._error = error_code

    def add_object(self, obj):
        type_ = obj.__class__.__name__.lower()
        pk = obj.get_primary_key()
        self.data[type_][pk] = obj

    @property
    def error(self):
        if self._error is not None:
            return self._error
        raise AttributeError
