from django.shortcuts import render, redirect
from django.db import connection
from webApp.forms import  ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# def home(request):
#     post = []
#     cursor = connection.cursor()
#     cursor.execute('select eno, ename from TESTAPP_EMPLOYEE')
#     row = cursor.fetchall()
#     for r in row:
#         post.append({'eno':r[0], 'ename':r[1]})
#     return render(request, "webApp/base.html", {'row':post})


def home(request):
    return render(request, "webApp/home.html")

def about(request):
    return render(request, "webApp/about.html")

def services(request):
    return render(request, "webApp/services.html")



def email(subj, mess, recp):
    subject = subj
    message = mess
    email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['receiver@gmail.com',]
    recipient_list = [recp, ]
    send_mail( subject, message, email_from, recipient_list )


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            addr = form.cleaned_data['address']
            comp = form.cleaned_data['company']
            subj = form.cleaned_data['subject']
            cont = str (form.cleaned_data['contact'])
            mess = form.cleaned_data['message']
            mess = 'Received Message From ' + name + ' Address - ' + addr + \
                   ' Company - ' + comp + ' Contact - '  + cont + ' Message is - ' + mess
            recp = 'vinod.msssoft@gmail.com'
            form.save()
            email(subj, mess, recp)
            return redirect('/')
    return render(request, "webApp/contact.html", {'form':form})


