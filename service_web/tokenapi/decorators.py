# @Author: Manuel Rodriguez <valle>
# @Date:   20-Jul-2017
# @Email:  valle.mrv@gmail.com
# @Filename: decorators.py
# @Last modified by:   valle
# @Last modified time: 05-Sep-2017
# @License: Apache license vesion 2.0


from functools import wraps
from base64 import b64decode


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from tokenapi.http import JsonResponseForbidden

def token_required(view_func):
    """Decorator which ensures the user has provided a correct user and token pair."""

    @csrf_exempt
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = None
        token = None
        basic_auth = request.META.get('HTTP_AUTHORIZATION')

        user = request.POST.get('user', request.GET.get('user'))
        token = request.POST.get('token', request.GET.get('token'))
        if not (user and token) and basic_auth:
            auth_method, auth_string = basic_auth.split(' ', 1)

            if auth_method.lower() == 'basic':
                auth_string = b64decode(auth_string.strip())
                user, token = auth_string.decode().split(':', 1)

        if not (user and token):
            return JsonResponseForbidden("Must include 'user' and 'token' parameters with request.")

        user = authenticate(pk=user, token=token)
        if user:
            request.user = user
            return view_func(request, *args, **kwargs)

        return JsonResponseForbidden("Must include 'user' and 'token' parameters with request.")
    return _wrapped_view
