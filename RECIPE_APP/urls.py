from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    path("userchoice/",userchoice,name="userchoice"),
    path("recipesearch/",recipesearch,name="recipesearch"),
    path("about/",about,name="about"),
    path("meals/",meals,name="meals"),
    path("add/",add,name="add"),
    path("recipe/",recipe,name="recipe"),
    path("recipe1/",recipe1,name="recipe1"),
    path("userrecipe/",userrecipe,name="userrecipe"),
    path("payment/",payment,name="payment"),
]