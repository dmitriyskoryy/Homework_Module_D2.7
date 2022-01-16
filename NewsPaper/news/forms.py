from django.forms import ModelForm, ComboField
from .models import *


# Создаём модельную форму
class NewsForm(ModelForm):


    # в класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'postCategory',]



