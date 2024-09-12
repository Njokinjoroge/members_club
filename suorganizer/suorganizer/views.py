from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_root(request):
    url_path= reverse("blog_post_list")
    return HttpResponseRedirect(url_path)  # Redirect to the root URL of the blog app
