from django.db import models
from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

# Create your models here.









# class Rost(models.Model):
#     title = models.CharField(max_length=150, db_index=True)
#     slug = models.SlugField(max_length=150, blank=True, unique=True)
#     body = models.TextField(blank=True, db_index=True)
#     date_pub = models.DateTimeField(auto_now_add=True)
#     tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
#     img = models.ImageField(null=True, upload_to="images/",
#         verbose_name=u'Your Photo')
#     def get_absolute_url(self):
#         return reverse('post_detail_url', kwargs={'slug':self.slug})
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = gen_slug(self.title)
#         super().save(*args, **kwargs)
#
#     def get_update_url(self):
#         return reverse('post_update_url', kwargs={'slug':self.slug})
#
#     def get_delete_url(self):
#         return reverse('post_delete_url', kwargs={'slug':self.slug})
#
#
#
#     def __str__(self):
#         return '{}'.format(self.title)
#
#     class Meta:
#         ordering = ['-date_pub']
