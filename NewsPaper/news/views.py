#  views.generic позволит выводить все объекты из БД в браузер "в HTML"
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод


from .models import *
from .filters import PostFilter # импортируем недавно написанный фильтр
from datetime import datetime
from .forms import NewsForm # импортируем нашу форму

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
    form_class = NewsForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    # В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные,
    # к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        context['form'] = NewsForm()
        return context



    def post(self, request, *args, **kwargs):
        # берём значения для новости из POST-запроса отправленного на сервер
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'newsone.html'
    queryset = Post.objects.all()


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



#
# class PostDetail(DetailView):
#     model = Post
#     template_name = 'newsone.html'
#     context_object_name = 'newsone'

