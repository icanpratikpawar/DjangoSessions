from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Login, Books
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
import library_management.settings as lib


def facebook(request):
    return HttpResponseRedirect("http://facebook.com")


def twitter(request):
    return HttpResponseRedirect("http://twitter.com")


def email_verify(request):
    return render(request, 'emailverify.html')


def send_email(request):
    send_mail("Hello Dada", "This is my first automated message\n\nhttp://127.0.0.1:8000/",
              lib.EMAIL_HOST_USER, [request.POST['send_email']])
    return redirect('/')


def logout(request):
    del request.session["user"]
    # return render(request, 'index.html', {'text': 'This is my text & I am its creator'})
    return redirect('/')


def index(request):
    if "user" in request.session:
        return redirect("/home")
    else:
        # Starting page of my website
        return render(request, 'index.html')


def home(request):
    # Method to verify the right login details by admin
    if "user" not in request.session:
        a = Login.objects.filter(
            user_name=request.POST['username'], pass_word=request.POST['pswd'])
        if a:
            request.session["user"] = a[0].user_name
            return render(request, "home.html", {'user': request.session["user"]})
        else:
            return HttpResponse("Errorr")
    else:
        # return render(request, 'index.html', {'text': 'This is my text & I am its creator'})
        print("Hello")
        print(request.session.get_expiry_date())
        return render(request, "home.html", {'user': request.session["user"]})


def books_validate(request):
    book_name = request.POST['bookname']
    author_name = request.POST['authorname']
    book_type = request.POST['booktype']
    Books(book_name=book_name, author_name=author_name,
          book_type=book_type).save()
    # return render(request, 'home.html', {'details': 'Books Details Submitted Succesfully'})
    return redirect("/home")


def book_view(request):
    query = {'books': Books.objects.all()}  # [0:2]
    return render(request, 'bookview.html', query)


def delete_record(request, id=None):
    Books.objects.filter(id=id).delete()
    querys = {'Delete': 'Record Deleted Succesfully!'}
    # return render(request, 'bookview.html',querys)
    return redirect('/bookview')


def update(request, id):
    return render(request, 'update-record.html', {'id': id, 'user': request.session["user"],
                                                  'books': Books.objects.get(id=id)})


def update_record(request, id=None):
    a = Books.objects.filter(id=id)
    if a:
        a.update(book_name=request.POST['bookname'],
                 author_name=request.POST['authorname'],
                 book_type=request.POST['booktype'])
    else:
        return HttpResponse("ERRORS")
    return redirect('/bookview')
