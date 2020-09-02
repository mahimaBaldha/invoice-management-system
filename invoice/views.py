from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
from invoice.forms import FileForm, InvoiceForm


# def home(request):
#     return render(request, "home.html")
from invoice.models import Invoice


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = auth.authenticate(username=uname, password=pwd)

        if user is not None:
            auth.login(request, user)
            request.session["user"] = user.username
            # print(request.session["user"])
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        print("request came for get!!")
        return render(request, "login.html")

def register(request):

    if request.method == 'POST':
        print("Request came for post")
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd2 = request.POST['confirm_password']

        if(pwd == pwd2):
            if(User.objects.filter(username=uname).exists()):
                messages.info(request, "User already exists")
                return redirect('/')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, "Email taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email, password=pwd)
                user.save();
                messages.info(request, "User created")
                return redirect('login')
        else:
            messages.info(request, "Password is not matching")
            return redirect('/')
    else:
        print("request came for get!!")
        return render(request, "register.html")

# def home(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             user_session = request.session["user"]
#             user = User.objects.get(username=user_session)
#             print(user)
#             # form.cleaned_data["pdf_copy"]
#             initial_obj = form.save()
#             # print(form.cleaned_data["pdf_copy"])
#             # pdf_path = 'invoice/pdfs/'+''+ form.cleaned_data["pdf_copy"]
#             # print(initial_obj.pdf_copy) => invoice/pdfs/190130107007_sem3A_DS_practical6_fjTC8Lk.pdf
#             # print(initial_obj.pdf_copy.url) => /media/invoice/pdfs/190130107007_sem3A_DS_practical6_fjTC8Lk.pdf
#             invoice = Invoice()
#             invoice.pdf_copy = initial_obj.pdf_copy
#             invoice.date = initial_obj.created_at
#             invoice.agent = user
#             invoice.save()
#             # print(invoice.pdf_copy) => invoice/pdfs/190130107007_sem3A_DS_practical6_3bnrPqW.pdf
#             # print(invoice.pdf_copy.url) => /media/invoice/pdfs/190130107007_sem3A_DS_practical6_fjTC8Lk.pdf
#             return redirect('home')
#     else:
#         form = FileForm()
#     return render(request, 'home.html', {
#         'form': form
#     })


def home(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = auth.authenticate(username=uname, password=pwd)

        if user is not None:
            auth.login(request, user)
            request.session["user"] = user.username
            # print(request.session["user"])
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        print("request came for get!!")
    return render(request, "login.html")

def demo(request):
    return render(request, "demo.html", {})