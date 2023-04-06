
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="home")
    path('api/get-quiz/' , views.get quiz , name="get_quiz")
    path('quiz')
]

