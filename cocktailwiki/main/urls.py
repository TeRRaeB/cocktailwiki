from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load-more-posts/', views.load_more_posts, name='load_more_posts'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('moderator-panel/', views.moderator_panel, name='moderator_panel'),
    path('change-status/<int:post_id>/<int:status>/', views.change_status, name='change_status'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
]
