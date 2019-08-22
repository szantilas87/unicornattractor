from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        contact = Contact(name=name, email=email,
                          message=message, user_id=user_id)
        contact.save()

        send_mail(
            'Contact request',
            "A new contact request has been made by " + email + " .Please log in to the admin panel for more info",
            'flaskmail123@gmail.com',
            ['flaskmail123@gmail.com','otheremail@somewhere.com'],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent')
        return redirect('home')

def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']

        send_mail(
            'Newsletter request',
            "A new newslettrt request has been made by " + email + " .",
            'flaskmail123@gmail.com',
            ['flaskmail123@gmail.com','otheremail@somewhere.com'],
            fail_silently=False,
        )
        messages.success(request, 'Your request has been sent')

        return redirect('home')
