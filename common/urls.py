from django.contrib import admin
from django.urls import path, include
from . import views

# localhost:8000/common/popup/comp/seatmap/1
urlpatterns = [
    path('popup/comp/foodtruck/<int:pk>' , views.comp_foodtruck , name="popup_comp_foodtruck"),
    path('popup/comp/seatmap/<int:pk>' , views.comp_seatmap , name="popup_comp_seatmap"),
]