from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .utils import *
from .models import *
from .forms import TagForm, PostForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Q
from blogengine.settings import STATIC_URL
import os
def posts_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Rost.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Rost.objects.all()


    paginator = Paginator(posts, 4)



    page_number = request.GET.get('page', 1)
    page= paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next ():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    my_picture = os.path.join('media', 'img/LOGO.png')

    context = {
        'page_object' : page,
        'is_paginated' : is_paginated,
        'next_url' : next_url,
        'prev_url' : prev_url,
        'my_picture' : my_picture,
    }

    return render(request, 'blog/index.html', context=context)


class PostDetail(ObjectDetailMixin, View):
    cl = 'post'
    model = Rost
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     post = get_object_or_404(Rost, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post':post})
class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form':form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form':bound_form})


class TagDetail(ObjectDetailMixin, View):
    cl = 'tag'
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag':tag})
    #

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Rost
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact = slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form':bound_form, 'tag':tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact = slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag':tag})
class TagDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_delete_form.html', context={'tag':tag})
    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))


class PostDelete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        post = Rost.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_delete_form.html', context={'post':post})
    def post(self, request, slug):
        post = Rost.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model =TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

    # def get(self, request):
    #     form = TagForm
    #     return render(request, 'blog/tag_create.html', context={'form':form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form':bound_form})
    #


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})
