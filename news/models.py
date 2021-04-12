from django.db import models


class News (models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%y%m%d/', verbose_name='Фотография',blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация новости')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title



#id -INT
#title - Varchar
#content - Text
#created_at - DataTime
#update_at -DataTime
#photo - Image
#is_published -Boolean