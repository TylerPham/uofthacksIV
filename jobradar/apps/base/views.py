"""Views for the base app"""

from django.shortcuts import render
from django.http import HttpResponse

from forms import QueryForm

def home(request):
    """ Default view for the root """
    form = QueryForm()
    return render(request, 'base/home.html', {'form': form})