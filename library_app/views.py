from django.shortcuts import redirect, render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Login, Books
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.urls import resolve

# Decorators function to prohibit illegal access to
b = ""


def prohibit_url_access(func):
    def wrap(request, *args, **kwargs):
        if "user" in request.session:
            return func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


# def check_url(func):
#     def wrap(request, *args, **kwargs):
#         if resolve(request.path_info).url_name == "index" and "user" in request.session:
#             return redirect('/home')
#         else:
#             print("hii")
#     return wrap


def facebook(request):
    return HttpResponseRedirect("http://facebook.com")


def twitter(request):
    return HttpResponseRedirect("http://twitter.com")


def password_reset(request, user_name):
    a = Login.objects.filter(user_name=user_name)
    if a:
        a.update(pass_word=request.POST['pswd'])
        return render(request, 'index.html')


def password_change(request, user_name):
    a = Login.objects.filter(user_name=user_name)
    if a:
        return render(request, 'password_change.html', {'user_name': user_name})
    else:
        pass


def email_verify(request):
    # Class(Object) to get the url name
    current_url = resolve(request.path_info).url_name
    if current_url == "emailverify":
        return render(request, 'emailverify.html')


def send_email(request):
    a = Login.objects.filter(email_id=request.POST['send_email'])
    if a:
        b = "http://127.0.0.1:8000/password_change/"+a[0].user_name
        send_mail("Hello "+a[0].user_name, "This is an automated message, It A password reset for your account was requested. Please click the button below to change your password.\n "+b,
                  settings.EMAIL_HOST_USER, [request.POST['send_email']])
        return render(request, 'index.html', {'msg': 'Succesfully send the reset password message'})
    else:
        return HttpResponse("!!..Not Registered..!!")


@prohibit_url_access
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
        try:
            a = Login.objects.filter(
                user_name=request.POST['username'], pass_word=request.POST['pswd'])
            if a:
                request.session["user"] = a[0].user_name
                return render(request, "home.html", {'user': request.session["user"]})
            else:
                return render(request, 'index.html', {'User': 'Check the username and password'})
        except Exception:
            raise PermissionDenied

    else:
        return render(request, "home.html", {'user': request.session["user"]})


@prohibit_url_access
def books_validate(request):
    book_name = request.POST['bookname']
    author_name = request.POST['authorname']
    book_type = request.POST['booktype']
    Books(book_name=book_name, author_name=author_name,
          book_type=book_type).save()
    # return render(request, 'home.html', {'details': 'Books Details Submitted Succesfully'})
    return redirect("/home")


@prohibit_url_access
def book_view(request):
    query = {'books': Books.objects.all()}  # [0:2]
    return render(request, 'bookview.html', query)


@prohibit_url_access
def delete_record(request, id=None):
    Books.objects.filter(id=id).delete()
    querys = {'Delete': 'Record Deleted Succesfully!'}
    # return render(request, 'bookview.html',querys)
    return redirect('/bookview')


@prohibit_url_access
def update(request, id):
    return render(request, 'update-record.html', {'id': id, 'user': request.session["user"],
                                                  'books': Books.objects.get(id=id)})


@prohibit_url_access
def update_record(request, id=None):
    a = Books.objects.filter(id=id)
    if a:
        a.update(book_name=request.POST['bookname'],
                 author_name=request.POST['authorname'],
                 book_type=request.POST['booktype'])
    else:
        return HttpResponse("ERRORS")
    return redirect('/bookview')
