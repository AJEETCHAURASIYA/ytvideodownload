from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    # path('',views.download,name='download'),
    # path('aboutus/',views.aboutus,name='aboutus'),
    # path('registration/',views.registration,name='registration'),
    # path('login/',views.login,name='login'),
    # path('contactus/',views.contactus,name='contactus'),
]
