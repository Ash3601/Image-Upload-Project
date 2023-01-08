from . import views
from django.urls import path
from .models import Image
from django.http import JsonResponse
from django.views.generic import View
from django.db import models
python3 - m pip install Django

mkdir project
cd project
django-admin startproject project

cd project
django-admin startapp quickstart

'''
To build an image uploading website with Django as the backend and Angular as the frontend, you can follow these steps:

Set up a Django project and create a Django app for the image uploading functionality.

Create a model in Django to store information about the images that are uploaded, such as the image file, title, and description.

Set up Django's authentication system to handle user registration and login.

Use Django's cache framework to cache data that is expensive to compute or retrieve, such as the list of images for a logged-in user.

Create class-based views in Django to handle the HTTP requests for the image uploading functionality.

Use Angular to build the frontend for the image uploading website. You can create a login and signup screen using Angular forms.

Create a component in Angular to display the list of images uploaded by the logged-in user in a 4x4 grid. Each cell should display the image and its title.

Create a component in Angular to handle the image uploading functionality. This component should have a form that asks the user to select an image file from their local system, enter a title and description for the image, and submit the form to send a request to the Django backend to upload the image.

Create a component in Angular to display the details of an image when it is clicked, including the image, title, and description. This component should also have an option to delete the image.

Test the image uploading website to make sure it is working as expected. You can add error handling to the backend and frontend to handle any issues that may arise.

'''


# models.py


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.TextField()


# views.py


class ImageUploadView(View):
    def post(self, request):
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        image_obj = Image.objects.create(
            image=image, title=title, description=description)
        return JsonResponse({'id': image_obj.id})


class ImageListView(View):
    def get(self, request):
        images = Image.objects.all()
        data = []
        for image in images:
            data.append({
                'id': image.id,
                'title': image.title,
                'description': image.description
            })
        return JsonResponse({'images': data})


class ImageDetailView(View):
    def get(self, request, image_id):
        image = Image.objects.get(id=image_id)
        data = {
            'id': image.id,
            'title': image.title,
            'description': image.description,
            'image_url': image.image.url
        }
        return JsonResponse(data)


class ImageDeleteView(View):
    def delete(self, request, image_id):
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'deleted': True})


# urls.py

urlpatterns = [
    path('images/', views.ImageListView.as_view(), name='image_list'),
    path('images/upload/', views.ImageUploadView.as_view(), name='image_upload'),
    path('images/<int:image_id>/',
         views.ImageDetailView.as_view(), name='image_detail'),
    path('images/<int:image_id>/delete/',
         views.ImageDeleteView.as_view(), name='image_delete'),
]


sudo npm uninstall - g @ angular/cli
sudo npm cache clean
sudo npm install - g @ angular/cli@8.3.25


ng new frontend

source ./env/bin/activate
