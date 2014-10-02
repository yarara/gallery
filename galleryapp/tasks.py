from celery import task
from celery.task import periodic_task
from celery.task.schedules import crontab
from django.core.mail import send_mail, EmailMessage
from gallery.settings import *
from galleryapp.models import *

@task
def send_function(user, args):
    args['req'] = user
    useri = User.objects.get(username = user)
    args['mail'] = useri.email
    message = EmailMessage('Архив изображений', '', MANAGER_FROM_EMAIL, [useri.email])
    args['from'] = MANAGER_FROM_EMAIL
    args['qwe'] = useri
    try:
        im = Image.objects.filter(user = useri)
        args['im1'] = im
    except:
        args['notuser'] = 'Нет файлов для отправки'
    else:
        for i in im:
            args['qwe1'] = message.attach_file(i.image.path)
    
    return args