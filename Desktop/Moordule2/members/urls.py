from django.urls import path
from .views import index, new, file

app_name="members"

urlpatterns = [
    path("", index, name="index"),        
    path("new/", new, name="new"),        
    path("<int:id>", file, name="file"),        
]