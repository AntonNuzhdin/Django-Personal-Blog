from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .models import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.



def home(request):
    return render(request, 'home/index.html')
