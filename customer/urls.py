from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('order/', views.order_view, name='order'),
]