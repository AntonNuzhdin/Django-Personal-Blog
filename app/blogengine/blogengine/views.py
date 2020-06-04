from django.shortcuts import redirect

def redirect_blog(requesr):
    return redirect('posts_list_url', permanent=True)
