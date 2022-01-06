from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view()), # as_view говорит что представление PostList, будет представлен ввиде представления
    path('search', PostSearch.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]