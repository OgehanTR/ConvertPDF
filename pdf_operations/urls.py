from django.urls import path
from . import views

urlpatterns = [
    path('pdf_merge/', views.pdf_merge, name='pdf_merge'),
    path('convert_to_pdf/', views.convert_to_pdf, name='convert_to_pdf'),
]
