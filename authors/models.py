from django.db import models
from django.template.defaultfilters import slugify


class Authors(models.Model):
    """Модель авторов"""
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=80)
    patronymic = models.CharField('Отчество', max_length=80, blank=True)
    biography = models.TextField('Биография', blank=True)
    pseudonym = models.CharField('Псевдоним', max_length=100, blank=True)
    slug = models.SlugField('Поле для url', help_text='Пример: denis-voloshin', blank=True, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

#    def get_absolute_url(self):
#        return reverse('author-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["surname"]
        db_table = 'authors'
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return "%s %s" % (self.surname, self.name)

    def save(self):
        if not self.id:
            newslug = '{0} {1}'.format(self.name, self.surname)
            self.slug = slugify(newslug)
        super(Authors, self).save()
