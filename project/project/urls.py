from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path("accounts/", include("allauth.urls")),  # Оставили только allauth
   path('news/', include('commonapp.urls_news')),
   path('articles/', include('commonapp.urls_articles')),
]
