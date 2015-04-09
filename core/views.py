from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
import core.models as cm

# Create your views here.

#Price Estimator

#Guest List

#Invitations

#Tokenized from

#Public Wedding Page


class LandingView(ListView):
    model = cm.Chapter
    queryset = cm.Chapter.objects.order_by('order')
    template_name = 'base/index.html'