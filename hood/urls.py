from django.urls import path
from . import views



urlpatterns = [
    path('',views.index ,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='index'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hood, name = 'hood'),
    path('hood/<str:name>',views.single_hood,name='single_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    path("create_post", views.create_post, name="create_post"), 
    path("posts/", views.posts, name="posts"),
    path('profiles/', views.profiles, name = 'profiles'),
    path("businesses/", views.businesses, name="businesses"),
    
]