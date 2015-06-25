# -*- mode: python; coding: utf-8; -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class User(object):
    def __init__(self, uid, email):
        self.uid = uid
        self.email = email

    def get_primary_key(self):
        return self.uid
