from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from customer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('aboute/', Aboute.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('order/', Order.as_view(), name='order'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('admin/menu/', AdminMenuView.as_view(), name='admin-menu'),
    path('admin/menu/create/', MenuCreate.as_view(), name='admin-menu-create'),
    path('admin/menu/<int:pk>/update/', MenuUpdate.as_view(), name='admin-menu-update'),
    path('admin/menu/<int:pk>/delete/', MenuDelete.as_view(), name='admin-menu-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
