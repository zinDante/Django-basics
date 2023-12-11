from django.urls import path
from . import views

urlpatterns= [
    # path("",views.index,name="index"),
    path("", views.students_view, name='home'),
    path("model/",views.datashow_model,name = 'models')
]