from django.contrib import admin
from . import views
from django.urls import path

app_name = 'finalapp'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('add', views.add, name='add'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
    path('review', views.review, name='review'),
    path('category/<str:genre>/', views.category, name='category'),
    path('search', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/add_category/', views.add_category, name='admin_add_category'),
    path('admin/add_or_delete_movie/', views.add_or_delete_movie, name='admin_add_or_delete_movie'),
    path('admin/view_users/', views.view_users, name='admin_view_users'),
    path('admin/delete_user/<int:user_id>/', views.delete_user, name='admin_delete_user'),
    path('admin/', admin.site.urls),

]
