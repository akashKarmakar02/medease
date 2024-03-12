from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.signup),
    path('sign-in', views.signin),
    path('sign-out', views.signout)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
