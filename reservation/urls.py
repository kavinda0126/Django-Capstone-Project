from django.urls import path
from .views import index,bookingview,menuview


urlpatterns=[

    path('',index,name='index'),
    path('menu/',menuview.as_view()),
    path('booking/',bookingview.as_view())

]