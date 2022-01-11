from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view()), # as_view говорит что представление PostList, будет представлен ввиде представления
    path('<int:pk>/', PostDetailView.as_view(), name='news_detail'), # Ссылка на детали товара
    path('search', PostSearch.as_view()),
    # path('newsone/<int:pk>', PostDetail.as_view()),
]