from django.urls import path
from . import views
# from recipes.views import home


urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe)
]
