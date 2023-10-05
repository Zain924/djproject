from django.shortcuts import render, HttpResponse
from datetime import datetime
from app.models import contact, Projects, about, CV, Images
from django.core.mail import send_mail
from django.http import FileResponse
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    images = Images.objects.all()

    home_image = None
    about_image = None

    for image_obj in images:
        if not home_image and image_obj.home_image:
            home_image = image_obj.home_image
        if not about_image and image_obj.about_image:
            about_image = image_obj.about_image


    
    about_objs = about.objects.all()
    about_us_list = []

    for about_obj in about_objs:
        about_us = {
            'name': about_obj.name,
            'email': about_obj.email,
            'phone': about_obj.phone,
            'location': about_obj.location
        }
    about_us_list.append(about_us)


    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        Contact = contact(name = name , email = email , desc = desc , date = datetime.today())
        Contact.save()

        subject = 'New Form Submission from Your Website'
        message = f'Name: {name}\nEmail: {email}\nMessage: {desc}'
        from_email = 'pzainchadury9246@gmail.com'  # Use the same email as EMAIL_HOST_USER        
        recipient_list = ['zainnii9246@gmail.com']  # Your personal email address

        send_mail(subject, message, from_email, recipient_list)

    projects = Projects.objects.all()

    return render (request , 'index.html' , {'projects': projects , 'about_us':about_us , 'home_image': home_image , 'about_image': about_image})


def add(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio1.html', {'projects': projects })


def download_cv(request):
    # Retrieve the CV object (assuming you have only one CV object)
    cv = get_object_or_404(CV)

    if cv.cv_file:
        response = FileResponse(cv.cv_file.open('rb'))
        response['Content-Type'] = 'application/pdf'  # Adjust the content type if your CV is in a different format
        response['Content-Disposition'] = 'attachment; filename="cv_download.pdf"'
        return response

    return HttpResponse("CV file not found")

