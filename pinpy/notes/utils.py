# Дополнительные вспомогательные классы.
import datetime
from importlib import import_module

from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.models import Session
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin


class Mixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        return context


'''class KeepLoggedInMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated or not settings.KEEP_LOGGED_KEY in request.session:
            return
        if request.session[settings.KEEP_LOGGED_KEY] != date.today():
            request.session.set_expiry(timedelta(days=settings.KEEP_LOGGED_DURATION))
            request.session[settings.KEEP_LOGGED_KEY] = date.today()
        return'''

'''class CustomSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        engine = import_module(settings.SESSION_ENGINE)
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        request.session = engine.SessionStore(session_key)
        if not request.session.exists(request.session.session_key):
            request.session.create()'''