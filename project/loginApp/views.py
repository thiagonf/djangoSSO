# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import requests

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic.base import TemplateView
from jose.exceptions import JWTError

import django_keycloak.services.oidc_profile
import django_keycloak.services.remote_client


logger = logging.getLogger(__name__)


class Home(TemplateView):
    template_name = 'home.html'

class Permission(PermissionRequiredMixin, TemplateView):
    raise_exception = True
    template_name = 'permission.html'
    permission_required = 'some-permission'
