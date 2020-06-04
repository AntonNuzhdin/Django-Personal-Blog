from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import *

class ObjectDetailMixin:
    model = None
    template = None
    cl = None
    def get(self, request, slug):

        obj = get_object_or_404(self.model, slug__iexact=slug)

        return render(request, self.template, context={self.cl:obj, 'admin_object':obj, 'detail':True})

class ObjectCreateMixin:
    form_model = None
    template = None




    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form':form})

    def post(self, request):
        bound_form = self.form_model(request.POST, request.FILES)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form':bound_form})
class ObjectUpdateMixin:
    model = None
    model_form = None
    templatel = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower():obj})
