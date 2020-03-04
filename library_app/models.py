from django.db import models

# Create your models here.
class Login(models.Model):
    user_name=models.TextField(blank=True)
    pass_word=models.TextField()
    email_id=models.EmailField(max_length=255, blank=False)
    current_date=models.DateTimeField(auto_now_add=True)
    
class Books(models.Model):
    book_name = models.TextField(blank = True)
    author_name = models.TextField(blank = True)
    book_type = models.TextField(blank = True)

class Supplier(models.Model):
    supplier_name = models.TextField(blank = True)
    address = models.TextField(blank = True)
    contact_number =  models.TextField(blank = True)
    tieup_with = models.TextField(blank = True)
    