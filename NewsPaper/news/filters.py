from django_filters import FilterSet, CharFilter, DateFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Author


# создаём фильтр
class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о новостях

    class Meta:
        model = Post
        fields = {
            # мы хотим чтобы нам выводило заголовок хотя бы отдалённо похожее на то, что запросил пользователь
            #'title': ['icontains'],
            'author': ['in'],
            'dateCreation': ['gt'],  # дата создания должна быть больше или равна той, что указал пользователь
            #'text': ['icontains'],  # мы хотим чтобы нам выводило текст статьи хотя бы отдалённо похожее на то, что запросил пользователь
        }

        #postCategory__name - таким образом, через __ мы обращаемся к полям связанного объекта

        #'dateCreation': ['gt'],  # дата создания должна быть больше или равна той, что указал пользователь
        # 'dateCreation': ['lt'],  # дата создания должна быть меньше или равнa той, что указал пользователь

#
#
# class My_AuthorFilter(FilterSet):
#     authorUser = CharFilter(method='user_filter')
#     class Meta:
#         model = Author
#         fields = ['authorUser']
#
#     def user_filter(self, queryset, name, value):
#         return queryset.filter(**{
#             name: value
#         })
#
#
# class My_DateFilter(FilterSet):
#     dateCreation = DateFilter()
#     class Meta:
#         model = Post
#         fields = ['dateCreation']

# class DataFilter(FilterSet):
#     date = DateFromToRangeFilter()
#     class Meta:
#         model = Post
#         fields = ['dateCreation']
