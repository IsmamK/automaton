from django.urls import path
from . import views

urlpatterns = [
    path("upload",views.upload,name='upload'),
    path("list",views.list,name='list'),
   path("download/<int:id>/", views.download, name='download')

]
