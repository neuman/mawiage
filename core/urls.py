from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as cv
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    url(r'^$', cv.LandingView.as_view()),
)
