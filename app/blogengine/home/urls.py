from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import *
urlpatterns = [

    url('', home, name='home'),



]
