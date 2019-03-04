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
from django.http import HttpResponseRedirect
from jose.exceptions import JWTError

import django_keycloak.services.oidc_profile
import django_keycloak.services.remote_client


logger = logging.getLogger(__name__)

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login'

class Login(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jwt = self.get_decoded_jwt()
        
        if jwt is not None:
            jwt=json.dumps(jwt, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            jwt = ""

        context['jwt'] = jwt
        return context  
    
    def get_decoded_jwt(self):
        if not hasattr(self.request.user, 'oidc_profile'):
            return None

        oidc_profile = self.request.user.oidc_profile
        client = oidc_profile.realm.client

        return client.openid_api_client.decode_token(
            token=oidc_profile.access_token,
            key=client.realm.certs,
            algorithms=client.openid_api_client.well_known[
                'id_token_signing_alg_values_supported']
        )


class Permission(LoginRequiredMixin, TemplateView):
    raise_exception = True
    template_name = 'permission.html'
    permission_required = 'some-permission'
