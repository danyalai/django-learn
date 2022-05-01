from django.urls import path
from . import views
urlpatterns = {
    path('about/', views.about_html),
    path('contactus/', views.contactus_html),
    path('home/', views.home_html),
}
