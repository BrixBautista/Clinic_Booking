from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


# Create your views here.

class HomeView(TemplateView):
    template_name =  'app/home.html'

class ContactView(TemplateView):
    template_name =  'app/contact.html'