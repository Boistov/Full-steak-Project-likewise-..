from django.urls import path
from . import views
from .views import MenuView, MenuSearch, MenuCreate, MenuUpdate, MenuDelete

urlpatterns = [
    path('order/', views.order_view, name='order'),
]