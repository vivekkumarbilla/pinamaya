from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('',index),
    path('about',about),
    path('products',products),
    path('product/<id>',product),
    path('gallery',gallery),
    path('contact-us',contact),
    path('subscribe',subscribe),
    url(r'^charcha-serviceworker(.*.js)$', charcha_serviceworker, name='charcha_serviceworker'),
    # url(r'^charcha-serviceworker(.*.js)$', views.charcha_serviceworker, name='charcha_serviceworker'),
]