from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView

from .models import Post


# Create your views here.

# *************************WILL REMOVE LATER*************************
# def ad_home(request):
#     return render(request, 'ad_home.html',{})   
# *******************************************************************

class ad_homeView(CreateView):
    model = Post
    template_name = 'ad_home.html'
    fields='__all__'

class homeView(ListView):
    model = Post
    template_name = 'home.html'
   

class pack_detailView(DetailView):
    model = Post
    template_name = 'pack_details.html'


