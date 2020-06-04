from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Rost

class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length = 50)
    # slug = forms.CharField(max_length = 50)
    #
    # title.widget.attrs.update({'class':'form-control'})
    # slug.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),}


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be like this')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug may be unique. We already have "{new_slug}"')
        else:
            return new_slug



    # def save(self):
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'],
    #                                  slug=self.cleaned_data['slug'])
    #     return new_tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Rost
        fields = ['title', 'slug', 'body', 'tags', 'img']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-control'}),
            }


        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('Slug may not be like this')
            return new_slug
