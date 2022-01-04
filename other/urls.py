from django.urls import path 
from . import views
# ######:8000/other/
urlpatterns = [ 
    path('',views.simple_view)
]