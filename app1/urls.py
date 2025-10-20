from django.contrib import admin
from django.urls import path, include
from app1 import views

admin.site.site_header = "FoodFest Admin"
admin.site.site_title = "FoodFest Portal"
admin.site.index_title = "Welcome to FoodFest Portal"

urlpatterns = [
    path("",views.index,name="homepage"),
    path("about",views.about,name="about"),
    path("menu",views.menu,name="menu"),
    path("contact",views.contact,name="contact"),
    path("egg_menu",views.egg_menu,name="egg_menu"),
    path("bbq_menu",views.bbq_menu,name="bbq_menu"),
    path("pizza_menu",views.pizza_menu,name="pizza_menu"),
    path("desserts_menu",views.desserts,name="desserts"),
    path("toast_menu",views.toast_menu,name="toast_menu"),
    path("pasta_menu",views.pasta_menu,name="pasta_menu"),
    path("locations",views.locations,name="locations"),
    path("delivery",views.delivery,name="delivery")
]