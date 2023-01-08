from rest_framework import viewsets

from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from .models import Image, Profile
from .serializers import ImageSerializer, ProfileSerializer


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


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def put(self, request, *args, **kwargs):
        image = request.data['image']
        title = request.data['title']
        description = request.data['description']
        Image.objects.create(image=image, title=title, description=description)
        return HttpResponse({'message': 'Image created'}, status=200)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer

#     def get(self, request, *args, **kwargs):
#         self.context['request'].user
#         user = request.data['user']
#         pwd = request.data['pwd']
#         obj = Profile.objects.find(user=user)
#         return HttpResponse({'password': obj.pwd}, status=200)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        print(request)
        print('Within get request')

    def put(self, request, *args, **kwargs):
        user = request.data['user']
        pwd = request.data['pwd']
        Profile.objects.create(user=user, pwd=pwd)
        return HttpResponse({'message': 'Image created'}, status=200)
