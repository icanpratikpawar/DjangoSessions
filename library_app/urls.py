from django.urls import path
from . import views

urlpatterns = [
    path('emailverify/', views.email_verify),
    path('home/', views.home, name="home"),
    path('sendemail/', views.send_email, name="sendemail"),
    path('', views.index),
    path('books_validate/', views.books_validate, name="bookvalidate"),
    path('bookview/', views.book_view, name="bookview"),
    path('bookview/update/<str:id>/', views.update, name="update"),
    path('update_record/<str:id>/', views.update_record, name="updatebooks"),
    path('delete_record/<str:id>/', views.delete_record, name="deletebooks"),
    path('logout/', views.logout),
    path('facebook/', views.facebook),
    path('twitter/', views.twitter),

]
