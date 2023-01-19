from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    slug = models.SlugField(max_length=40, unique=True, verbose_name="URL")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    def __str__(self):
        return self.title

    def is_search_result(self, search_title):
        str_title = str(self.title)
        if str_title.lower() == search_title.lower() or search_title.lower() in str_title.lower():
            return True
        else:
            return False

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Action(models.Model):
    action = models.CharField(max_length=100, verbose_name="Действие")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Время действия")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Действие"
        verbose_name_plural = "Действия"
