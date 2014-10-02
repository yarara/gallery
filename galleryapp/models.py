from django.db import models
from django.contrib.auth.models import User
from gallery import settings
#from account.compat import AUTH_USER_MODEL, receiver
from django.forms.models import modelform_factory
from django.db.models.signals import post_delete
from django.dispatch import receiver


AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

class Image(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name="account", verbose_name="user", blank = True)
    image = models.ImageField(upload_to='images', default='', verbose_name='Изображение')
    date_upload = models.DateField('Дата загрузки', auto_now_add = True)
    date_update = models.DateField('Дата обновления', auto_now =True)

    def __str__(self):
        return 'image {0} - user {1}'.format(self.image, self.user)

@receiver(post_delete, sender=Image)
def image_post_delete_handler(sender, **kwargs):
    image = kwargs['instance']
    storage, path = image.image.storage, image.image.path
    storage.delete(path)

ImageForm = modelform_factory(Image, fields=("image",),localized_fields = ('user',))

class Notes(models.Model):
    image_id = models.ForeignKey(Image, verbose_name = 'Изображение')
    user = models.ForeignKey(AUTH_USER_MODEL, related_name="user_id", verbose_name="user", default = 1, null = True, blank = True)
    text_note = models.TextField(default='', verbose_name='Изображение', blank = True)

    def __str__(self):
        return '{0}'.format(self.image_id)
