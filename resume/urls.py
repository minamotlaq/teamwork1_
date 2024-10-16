from django.urls import path
from . import views

urlpatterns = [
   path('',views.resume_view),
   path('detail/',views.resume_detail_view),
]
