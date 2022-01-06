#  views.generic позволит выводить все объекты из БД в браузер "в HTML"
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод


from .models import *
from .filters import PostFilter # импортируем недавно написанный фильтр
from datetime import datetime

# пишем представление
class PostList(ListView):
    # указываем модель, объекты которой будем выводить
    model = Post
    # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том,
    # как именно пользователю должны вывеститсь наши объекты
    template_name = 'news.html'
    # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самоу списку объектов через html-шаблон
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 10

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    # В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные,
    # к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context


# пишем представление
class PostSearch(ListView):
    # указываем модель, объекты которой будем выводить
    model = Post
    # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том,
    # как именно пользователю должны вывеститсь наши объекты
    template_name = 'search.html'
    # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самоу списку объектов через html-шаблон
    context_object_name = 'search'
    ordering = ['-id']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context




class PostDetail(DetailView):
    model = Post
    template_name = 'newsone.html'
    context_object_name = 'newsone'

