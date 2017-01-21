"""Views for the base app"""

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def query_location(request):
    return render(request, 'base/form.html')

# def post_new(request):
#     form = PostForm()
#     return render(request, 'query_location.html', {'form': form})
