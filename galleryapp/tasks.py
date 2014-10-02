from celery import task
from celery.task import periodic_task
from celery.task.schedules import crontab
from django.core.mail import send_mail, EmailMessage
from gallery.settings import *
from galleryapp.models import *

@task
def send_function(user, args):

    useri = User.objects.get(username = user)

    message = EmailMessage('Архив изображений', '', MANAGER_FROM_EMAIL, [useri.email])

    try:
        im = Image.objects.filter(user = useri)

    except:
        args['notuser'] = 'Нет файлов для отправки'
    else:
        for i in im:
            message.attach_file(i.image.path)
    
    return args
