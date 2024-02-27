from django.urls import path
from . import views

urlpatterns = [
    path('', views.album, name='album'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit_musician/<int:id>', views.edit_name, name='edit_musician'),
    path('delete/<int:id>', views.delete, name='delete'),
]
