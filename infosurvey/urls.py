from django.urls import path
from .views import waitlist_form

urlpatterns = [
    path('', waitlist_form, name='waitlist_form'),
]
