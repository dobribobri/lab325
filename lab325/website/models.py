from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy


# Create your models here.
class FileTypes:
    choices = (
        ('Файл PDF', 'Файл PDF'),
        ('Документ Word', 'Документ Word'),
        ('Документ Excel', 'Документ Excel'),
        ('Документ ODS', 'Документ ODS'),
        ('Изображение JPG/PNG/...', 'Изображение JPG/PNG/...'),
        ('ZIP-архив', 'ZIP-архив'),
        ('RAR-архив', 'RAR-архив'),
        ('', 'Другое')
    )


class PublicationTypes:
    choices = (
        ('Журнал', 'Журнал'),
        ('Материалы конференции (съезда, симпозиума)', 'Материалы конференции (съезда, симпозиума)'),
        ('Сборник (научных трудов)', 'Сборник (научных трудов)'),
        ('Препринт', 'Препринт'),
        ('Монография', 'Монография'),
        ('Автореферат', 'Автореферат'),
        ('Статья', 'Статья'),
        ('Иное', 'Иное')
    )


################################
class NewsBlock(models.Model):
    caption = models.CharField(verbose_name='Заголовок', max_length=254)

    annotation = models.TextField(verbose_name='Аннотация', null=True, blank=True)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    desc = models.TextField(verbose_name='Текст', null=True, blank=True)

    file = models.FileField(verbose_name='Прикрепить файл (извещение)', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    url = models.CharField(verbose_name='Ссылка', max_length=254, null=True, blank=True)

    def __str__(self):
        return "Новость - " + str(self.caption)

    class Meta:
        verbose_name = gettext_lazy("новость")
        verbose_name_plural = gettext_lazy("[Главная] Новости")


class AnnouncementConferenceBlock(models.Model):
    caption = models.CharField(verbose_name='Название конференции', max_length=254)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    when = models.CharField(verbose_name='Когда', max_length=254)
    where = models.CharField(verbose_name='Где', max_length=254)

    file = models.FileField(verbose_name='Прикрепить файл (извещение)', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)
    url = models.CharField(verbose_name='Ссылка', max_length=254, null=True, blank=True)

    def __str__(self):
        return "Анонс - " + str(self.caption)

    class Meta:
        verbose_name = gettext_lazy("анонс конференции")
        verbose_name_plural = gettext_lazy("[Главная] Конференции (анонсы)")


class AnnouncementSeminarBlock(models.Model):
    caption = models.CharField(verbose_name='Заголовок', max_length=254)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    when = models.CharField(verbose_name='Когда', max_length=254)
    where = models.CharField(verbose_name='Где', max_length=254)

    def __str__(self):
        return "Анонс - " + str(self.caption)

    class Meta:
        verbose_name = gettext_lazy("анонс семинара")
        verbose_name_plural = gettext_lazy("[Главная] Семинары (анонсы)")


class SeminarBlock(models.Model):
    caption = models.CharField(verbose_name='Заголовок', max_length=254)

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    when = models.CharField(verbose_name='Когда', max_length=254)
    where = models.CharField(verbose_name='Где', max_length=254)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    file = models.FileField(verbose_name='Прикрепить файл (решение)', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)

    def __str__(self):
        return "Семинар - " + str(self.caption)

    class Meta:
        verbose_name = gettext_lazy('объект \"Семинар (состоявшийся)\"')
        verbose_name_plural = gettext_lazy("[Главная] Семинары (состоявшиеся)")


################################
class GrantsBlock(models.Model):
    caption = models.CharField(verbose_name='Название', max_length=254)

    abbreviation = models.CharField(verbose_name='Код', max_length=254, null=True, blank=True)

    chief = models.CharField(verbose_name='Руководитель проекта', max_length=254)

    duration = models.CharField(verbose_name='Продолжительность', max_length=254)

    annotation = models.TextField(verbose_name='Аннотация', null=True, blank=True)

    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)

    def __str__(self):
        return "Грант - " + str(self.caption)

    class Meta:
        verbose_name = gettext_lazy('объект \"Грант (участие)\"')
        verbose_name_plural = gettext_lazy("[Исследования] Гранты (участие)")


class AchievementsBlock(models.Model):
    year = models.IntegerField(verbose_name='Год')

    desc = models.TextField(verbose_name='Перечисление достижений', null=True, blank=True)

    file = models.FileField(verbose_name='Прикрепить файл', null=True, blank=True)
    filetype = models.CharField(verbose_name='Тип файла', max_length=254, null=True, blank=True,
                                choices=FileTypes.choices)

    def __str__(self):
        return "Достижения - " + str(self.year)

    class Meta:
        verbose_name = gettext_lazy("достижения")
        verbose_name_plural = gettext_lazy("[Исследования] Достижения лаборатории")


################################
class LaboratoryMemberBlock(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=100)

    image = models.ImageField(verbose_name='Фотография (3x4)', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    def __str__(self):
        return "Сотрудник - " + str(self.fio)

    class Meta:
        verbose_name = gettext_lazy('объект \"Сотрудник лаборатории\"')
        verbose_name_plural = gettext_lazy("[Состав] Сотрудники лаборатории")


################################
class UrlBlock(models.Model):
    image = models.ImageField(verbose_name='Иконка', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    url = models.CharField(verbose_name='Ссылка', max_length=254)

    def __str__(self):
        return "Ссылка - " + str(self.url)

    class Meta:
        verbose_name = gettext_lazy('блок \"Полезная ссылка\"')
        verbose_name_plural = gettext_lazy("[Ссылки] Полезные ссылки")


################################
class CRFBlock(models.Model):
    image = models.ImageField(verbose_name='Иконка', null=True, blank=True)

    desc = models.TextField(verbose_name='Информация', null=True, blank=True)

    url = models.CharField(verbose_name='Ссылка', max_length=254)

    def __str__(self):
        return "Ссылка на ресурс - " + str(self.url)

    class Meta:
        verbose_name = gettext_lazy('блок \"Ресурс\"')
        verbose_name_plural = gettext_lazy("[Вычислительный центр] Ресурсы")


################################
class Publication(models.Model):
    authors = models.TextField(verbose_name='Авторы (Фамилия И.О.)',
                               help_text='Например: Егоров Д.П., Илюшин Я.А., Кутуза Б.Г., Аквилонова А.Б.')

    affiliations = models.CharField(verbose_name='Кол-во аффилиаций (через запятую)', max_length=254,
                                    null=True, blank=True,
                                    help_text='Например: 2, 3, 1, 2')

    authors_ire = models.TextField(verbose_name='Авторы с аффилиацией ИРЭ им. В.А. Котельникова РАН (Фамилия И.О.)',
                                   help_text='Например: Егоров Д.П., Кутуза Б.Г.', null=True, blank=True)

    name = models.TextField(verbose_name='Название публикации')

    pub_name = models.TextField(verbose_name='Наименования издания',
                                help_text='Например: IEEE Transactions on Geoscience and Remote Sensing')

    vol = models.CharField(verbose_name='Том', max_length=100,
                           null=True, blank=True, help_text='Например: 4')
    issue = models.CharField(verbose_name='Выпуск', max_length=100,
                             null=True, blank=True, help_text='Например: 2')
    no = models.CharField(verbose_name='Номер', max_length=100,
                          null=True, blank=True, help_text='Например: 10')
    pages = models.CharField(verbose_name='Страницы', max_length=100,
                             null=True, blank=True, help_text='Например: 264-273')

    pub_type = models.CharField(verbose_name='Вид издания', max_length=254,
                                choices=PublicationTypes.choices,
                                help_text='Выберите из выпадающего списка')

    date_year = models.CharField(verbose_name='Дата публикации', max_length=100,
                                 help_text='Например: 2021')

    grant = models.TextField(verbose_name='Финансирование', null=True, blank=True,
                             help_text='Введите код проекта РФФИ/РНФ/... или оставьте поле пустым, если работа ' +
                                       'выполнена по гос.заданию')

    doi = models.CharField(verbose_name='DOI', max_length=100, null=True, blank=True,
                           help_text='Вставьте идентификатор DOI или ссылку на https://www.doi.org/')

    issn = models.CharField(verbose_name='ISSN', max_length=100, null=True, blank=True)
    isbn = models.CharField(verbose_name='ISBN', max_length=100, null=True, blank=True)

    rsci = models.CharField(verbose_name='РИНЦ', max_length=100, null=True, blank=True,
                            help_text='Вставьте	eLIBRARY ID или ссылку на https://www.elibrary.ru/')
    wos = models.CharField(verbose_name='WoS', max_length=100, null=True, blank=True)
    scopus = models.CharField(verbose_name='Scopus', max_length=100, null=True, blank=True)

    edn = models.CharField(verbose_name='Код EDN', max_length=100, null=True, blank=True,
                           help_text='eLIBRARY Document Number (не путать с eLIBRARY ID)')
    springer = models.CharField(verbose_name='Springer', max_length=100, null=True, blank=True)
    ads = models.CharField(verbose_name='Astrophysics Data System', max_length=100, null=True, blank=True)
    msn = models.CharField(verbose_name='MathSciNet', max_length=100, null=True, blank=True)
    zbmath = models.CharField(verbose_name='zbMATH', max_length=100, null=True, blank=True)
    chemabs = models.CharField(verbose_name='Chemical Abstracts', max_length=100, null=True, blank=True)
    agris = models.CharField(verbose_name='Agris', max_length=100, null=True, blank=True)
    georef = models.CharField(verbose_name='GeoRef', max_length=100, null=True, blank=True)
    pubmed = models.CharField(verbose_name='PubMed', max_length=100, null=True, blank=True)

    bib_ref = models.TextField(verbose_name='Рекомендуемая библиографическая ссылка',
                               null=True, blank=True)

    fio_affiliation = models.TextField(verbose_name='Полные ФИО и аффилиации авторов',
                                       null=True, blank=True)

    def __str__(self):
        return "" + str(self.authors) + " " + str(self.name) + \
               " // " + str(self.pub_name) + ". " + str(self.date_year)

    class Meta:
        verbose_name = gettext_lazy('объект \"Публикация\"')
        verbose_name_plural = gettext_lazy("[!] Публикации")


################################
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    sex_choices = (
        ('м', 'муж.'),
        ('ж', 'жен.'),
    )
    sex = models.CharField(verbose_name='Пол', max_length=4, choices=sex_choices, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=100, null=True, blank=True)
    education = models.CharField(verbose_name='Образование', max_length=100, null=True, blank=True)
    degree = models.CharField(verbose_name='Ученая степень', max_length=100, null=True, blank=True)
    title = models.CharField(verbose_name='Ученое звание', max_length=100, null=True, blank=True)

    filled = models.BooleanField(verbose_name='Заполнены основные поля', default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = gettext_lazy("Профиль пользователя")
        verbose_name_plural = gettext_lazy("Профили пользователей")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
