from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
import datetime
from galleryapp.models import *
from django import forms
from django.core.mail import send_mail, EmailMessage
from gallery.settings import *
from celery.task import task
from galleryapp.tasks import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from galleryapp.serializers import UserSerializer, GroupSerializer



def index(request):
    args = {}
    try:
        im = Image.objects.all()
        args['im'] = im
    except:
        args['notuser'] = 'Галерея пуста.'
   
    try:
        args['username'] = User.objects.get(username = request.user)
    except:
        pass

    return render(request, 'gallery/index.html', args)


def registration(request):
    args = {}
    class UserCreateForm(UserCreationForm):
        email = forms.EmailField(required=True)
        
        class Meta:
            model = User
            fields = ( "username", "email", 'password1', 'password2' )

    class Meta:
        model = User
        fields = ( "username", "email" )
    args['form'] = UserCreateForm()

    if request.method == 'POST':
        new_user_form = UserCreateForm(request.POST)

        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'], password = new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return HttpResponseRedirect("/")
        else:
            args['form'] = new_user_form

    return render(request, 'gallery/register.html', args)

def login(request):
    args = {}
    args['form'] = AuthenticationForm()

    if request.method == 'POST':
        user = auth.authenticate(username =  request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/userdashboard/")
        else:
            args['form'] = user_form = AuthenticationForm()
            args['error'] = 'не верный пользователь или пароль'
            return render(request, 'gallery/login.html', args)

    return render(request, 'gallery/login.html', args)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def userdashboard(request):
    args = {}

    if request.method == 'POST':
        user = User.objects.get(username = request.user)
        if 'sendtoemail' in request.POST:
            r =send_function.apply_async(args = [request.user, args], countdown = 1)
            args['r'] = r.ready()
        else:            
            form = ImageForm(request.POST, request.FILES)
            f = form.save(commit = False)
            f.user = user
            f.save()

    try:
        args['im'] = Image.objects.filter(user = request.user)
    except:
        args['notuser'] = 'Галерея пуста.'
    
    try:
        args['username'] = User.objects.get(username = request.user)
    except:
        pass

    args['form'] = ImageForm()

    return render(request, 'gallery/userdashboard.html', args)

def imagebrowse(request, image_id):
    args = {}
    im = Image.objects.get(id = image_id)
    args['im'] = im
    if request.method == 'POST':
        if 'delimage' in request.POST:
            Image.objects.get(id = im.id).delete()
            return HttpResponseRedirect("/userdashboard")
        else:
            note = Notes(image_id_id = im.id, user = User.objects.get(username = request.user), text_note = request.POST['notearea'])
            note.save()

    try:
        image_note = Notes.objects.filter(image_id = im.id)
        args['image_note'] =  image_note
    except:
        args['image_note'] = ''
    
    try:
        args['username'] = User.objects.get(username = request.user)
    except:
        pass

    return render(request, 'gallery/image.html', args)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

