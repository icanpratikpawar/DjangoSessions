from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('emailverify/', views.email_verify,name="emailverify"),
    path('home/', views.home, name="home"),
    path('msg/', views.index, name="msg"),
    
    path('password_reset/<str:user_name>/', views.password_reset, name="password_reset"),
    path('password_change/<str:user_name>', views.password_change, name="passChange"),
    path('google_auth/', TemplateView.as_view(
        template_name='/home/pratik/Workspace/Djangoprograms/library_management/templates/gooogle-auth.html')),
    path('sendemail/', views.send_email, name="sendemail"),
    path('', views.index, name="index"),
    path('books_validate/', views.books_validate, name="bookvalidate"),
    path('bookview/', views.book_view, name="bookview"),
    path('bookview/update/<str:id>/', views.update, name="update"),
    path('update_record/<str:id>/', views.update_record, name="updatebooks"),
    path('delete_record/<str:id>/', views.delete_record, name="deletebooks"),
    path('logout/', views.logout),
    path('facebook/', views.facebook),
    path('twitter/', views.twitter),
]
