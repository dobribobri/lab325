from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy


# Create your models here.
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
        verbose_name = ugettext_lazy("Профиль пользователя")
        verbose_name_plural = ugettext_lazy("Профили пользователей")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
