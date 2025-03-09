from django.urls import path
from . import views  

app_name= 'app_main'
urlpatterns = [
    path('', views.home, name='home'),  
    path('add/', views.add_post, name='add-post'),
    path('details/<post_id>/', views.details, name='details'),
    path('update/<post_id>/', views.update, name='update'),
    path('delete/<post_id>/', views.delete, name='delete'),
    path('review/<post_id>/', views.review, name='review'),
    
]