from django.urls import path
from .views import OwnView

urlpatterns = [
    path('own/', OwnView.as_view(), name='main'),
]
