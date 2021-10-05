from django.urls import path
from .views import index # точка перед файлом импорта заставляет джанго искать файлы именно в данной директории
#asdd

urlpatterns = [
    path('hi/', index)
]