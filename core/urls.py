from django.urls import path

from .views import IndexView#, TestView

urlpatterns =[
    path('', IndexView.as_view(), name='index'),
#    path('teste/', TestView.as_view(), name='teste'),
]