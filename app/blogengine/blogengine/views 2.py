from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
import requests
import json

def redirect_blog(requesr):
    return redirect('posts_list_url', permanent=True)

def redirect_home(request):
    return redirect('home', permanent=True)

def redirect_yandex(request):
    return redirect('yandex', permanent=True)
