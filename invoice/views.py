from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from invoice.forms import FileForm, InvoiceForm
from django.core.mail import send_mail

from invoice.models import Invoice, Items



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username', False)
        pwd = request.POST.get('password', False)
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
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email, password=pwd, is_superuser=False)
                user.save();
                messages.info(request, "User created")
                return redirect('login')
        else:
            messages.info(request, "Password is not matching")
            return redirect('/')
    else:
        print("request came for get!!")
        return render(request, "register.html")


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
        context = {}
        if 'user' in request.session:
            user_session = request.session["user"]
            user = User.objects.get(username=user_session)
            if user.is_superuser:
                invoices = Invoice.objects.all()
                role = "Manager"
            else:
                invoices = Invoice.objects.filter(agent=user.id)
                role = "Agent"
            context = {'invoice': invoices, 'role': role}
            return render(request, "index.html", context)
        else:
            return redirect("login")


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect("/")


def uploadFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            if 'user' in request.session:
                user_session = request.session["user"]
                user = User.objects.get(username=user_session)
                print(user)
                pdf_name = form.cleaned_data["pdf_copy"]
                initial_obj = form.save()
                invoice = Invoice()
                invoice.pdf_copy = initial_obj.pdf_copy
                invoice.date = initial_obj.created_at
                invoice.agent = user
                invoice.save()
            return redirect("/create_invoice/"+str(invoice.id)+"/"+str(pdf_name))
        else:
            form = FileForm()
            return render(request, 'file_upload.html', {
                "form" : form
            })
    else:
        form = FileForm()
        return render(request, "file_upload.html", {
            "form" : form
        })

def createInvoice(request, id, pdf_name):

    if request.method == 'POST':

        invoices = Invoice.objects.filter(id=id)
        for invoice in invoices:
            invoice.invoice_number = request.POST.get('invoice_no') if request.POST.get('invoice_no') else None
            invoice.vendor_name = request.POST.get('vendor_name') if request.POST.get('vendor_name') else None
            invoice.date = request.POST.get('invoice_date') if request.POST.get('invoice_date') else None
            invoice.save()

        desc = request.POST.getlist('desc')
        qty = request.POST.getlist('qty')
        rate = request.POST.getlist('rate')

        for i in range(len(desc)):
            item = Items()
            item.desc = desc[i]
            item.qty = qty[i]
            item.rate = rate[i]
            item.invoice_id = id
            item.save()

        for invoice in invoices:
            if invoice.invoice_number and invoice.vendor_name is None:
                invoice.delete()

        # Email Functionality
        link = invoice.pdf_copy.url
        Manager = User.objects.get(is_superuser=True)
        send_mail(
            'New Invoice Generated',
            'This is the link for the new invoice generated'+link,
            'edunetwork000@gmail.com',
            [Manager.email],
            fail_silently=False
        )
        return redirect("/")
    else:
        invoice = Invoice.objects.filter(id=id)
        print(invoice)
        return render(request, "create_invoice.html", {"pk":id, "pdf_name":pdf_name})

