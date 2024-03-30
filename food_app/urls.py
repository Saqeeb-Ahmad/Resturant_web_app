from django.contrib import admin
from django.urls import path,include
from food_app import views
from food_website import settings
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food_app'

urlpatterns = [
    path('', views.landing_page, name="landing"),
    path('home/', views.home_page, name="home"),
    path('about/', views.about_page),
    path('services/', views.services_page),
    path('feedback/', views.feedback_view, name="feedback"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_page, name="logout"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)