from datetime import datetime

from django import forms
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import fields
from django.shortcuts import render,redirect, HttpResponse
from django.views import View

from home.forms import ImageForm
from home.models import Contact, Image, Videos
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

# Create your views here.
def image(request):
  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'image.html', {'form' : form})
  

def display_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        images = Image.objects.all() 
        return render((request, 'image.html',
                     {'images' : images}))

def success(request):
    return HttpResponse('successfully uploaded')


# class AddImageView(View):
#     form_class = ImageForm
#     initial = {'key':'value'}

# class AddProfileImageView(View):
# 	# form_class = ImageForm
# 	initial = {'key': 'value'}
# 	template_name = 'image.html'

	# def post(self, request, *args, **kwargs):
        
    #     form = ImageForm(request.POST, request.FILES)
        
    #     if form.is_valid():
    #         form.save()


def uploadfile_view(request):

    if request.method=='POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        filename, ext =str(f).split('.')
        file = fs.save(str(f),f)
        fileurl = fs.url(file)
        size = fs.size(file)
        print("f", f)
        print("fs", fs)
        print("file", file)
        print("fileurl", fileurl)
        print("filename", filename)
        print("ext", ext)
        print("size", size)


        context = {
            'fileurl': fileurl,
            'filename': filename,
            'ext': ext,
            'size': size
        }
        return render(request, 'pdf_viewer.html', context)

    else:
        return render(request, 'pdf_viewer.html')


def contact_list_view(request):
    
    contact_list = Contact.objects.all()
    context={
        'contact_list': contact_list,
    }
    
    return render(request, 'contact_list.html', context )


def show_contact_view(request, contact_id):

    contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact' : contact,
    }

    return render(request, 'show_contact.html', context )


def search_view(request):

    if request.method == "POST":
        searched = request.POST['searched']
        contact = Contact.objects.filter(name__contains = searched)

        context={
            'searched': searched,
            'contact' : contact
        }
        return render(request, 'search.html', context )
    
    else:

        context={
        }
        return render(request, 'search.html', context )