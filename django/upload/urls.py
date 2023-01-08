# from . import views
from django.urls import path
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import ImageViewSet, ProfileViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api/auth/', include('rest_framework.urls')),
]


# urlpatterns = [
#     path('images/', views.ImageListView.as_view(), name='image_list'),
#     path('images/upload/', views.ImageUploadView.as_view(), name='image_upload'),
#     path('images/<int:image_id>/',
#          views.ImageDetailView.as_view(), name='image_detail'),
#     path('images/<int:image_id>/delete/',
#          views.ImageDeleteView.as_view(), name='image_delete'),
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
