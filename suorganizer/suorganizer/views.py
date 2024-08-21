from django.http import HttpResponseRedirect


def redirect_root(request):
    return HttpResponseRedirect('/blog/')  # Redirect to the root URL of the blog app
