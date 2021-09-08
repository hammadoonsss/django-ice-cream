from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Videos
from django.contrib import messages

# Create your views here.



def index(request):


    context = {
        "variable": "This is the Dynamic Variable."
    }

    return render(request, "index.html", context)
    # return HttpResponse("This is Home Page. :) ")


def about(request):

    return render(request, "about.html")


def services(request):

    return render(request, "services.html")


def video(request):

    videos = Videos.objects.all()
    context = {
        'videos':videos
    }
    return render(request, "video.html", context)


def contact(request):


    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())

        contact.save()

        messages.success(request, 'You message has been sent!')

    return render(request, "contact.html")