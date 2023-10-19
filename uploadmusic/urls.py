from django.urls import path
from .views import UploadmusicView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', UploadmusicView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)