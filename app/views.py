from msilib.schema import ListView
from .models import *
from .forms import *
from django.http import HttpRequest, FileResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import cv2
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404


Menu = {
    "Загрузить изображение": 'upload_image',
    "Загрузить видео": 'upload_video',
}

def show_album(request, album_id):
    form_image = UploadImageForm
    form_video = UploadVideoForm()
    album = get_object_or_404(Album, id=album_id)
    imgs = album.image_ids.split(' ')
    vids = album.video_ids.split(' ')
    participants = album.participant_ids.split(' ')
    name = album.name
    for i in range(len(participants)):
        if participants[i].isdigit():
            participants[i] = int(participants[i])
    images = []
    videos = []
    for i in imgs:
        if i.isdigit():
            images.append(Image.objects.get(id=i))
    for i in vids:
        if i.isdigit():
            videos.append(Video.objects.get(id=i))
    users = User.objects.all()
    template_name = 'app/album.html'
    user_id = request.user.id

    if request.method == "POST" and album_id is not None and 'delete_photo' in request.POST:
        img_id = str(request.POST.get("delete_photo"))
        album = Album.objects.get(id=album_id)
        imgs = album.image_ids.split(' ')
        imgs.remove(img_id)
        album.image_ids = " ".join(imgs)
        album.save()
        return redirect("album", album_id=album_id)

    if request.method == "POST" and album_id is not None and 'delete_video' in request.POST:
        vid_id = str(request.POST.get("delete_video"))
        album = Album.objects.get(id=album_id)
        vids = album.video_ids.split(' ')
        vids.remove(vid_id)
        album.video_ids = " ".join(vids)
        album.save()
        return redirect("album", album_id=album_id)

    if request.method == "POST" and album_id is not None and 'delete_participant' in request.POST:
        participant_id = str(request.POST.get("delete_participant"))
        album = Album.objects.get(id=album_id)
        part_ts = album.participant_ids.split(' ')
        part_ts.remove(participant_id)
        album.participant_ids = " ".join(part_ts)
        album.save()
        return redirect("album", album_id=album_id)

    if request.method == "POST" and album_id is not None and 'add_photo' in request.POST:
        form_image = UploadImageForm(request.POST, request.FILES)
        album = Album.objects.get(id=album_id)
        if form_image.is_valid():
            try:
                img = form_image.save(commit=False)
                img.user_id = request.user.id
                img.save()
                album.image_ids += (str(img.id) + ' ')
                album.save()
                return redirect('album', album_id=album_id)
            except:
                form_image.add_error(None, "Ошибка загрузки")
    else:
        form_image = UploadImageForm()

    if request.method == "POST" and album_id is not None and 'add_video' in request.POST:
        form_video = UploadVideoForm(request.POST, request.FILES)
        album = Album.objects.get(id=album_id)
        if form_video.is_valid():
            try:
                vid = form_video.save(commit=False)
                vid.user_id = request.user.id
                vid.save()
                album.video_ids += (str(vid.id) + ' ')
                album.save()
                return redirect('album', album_id=album_id)
            except:
                form_video.add_error(None, "Ошибка загрузки")
    else:
        form_video = UploadVideoForm()

    if request.method == "POST" and album_id is not None and 'add_participant' in request.POST:
        id = str(request.POST.get("add_participant"))
        album = Album.objects.get(id=album_id)
        album.participant_ids += (' ' + id)
        album.save()
        return redirect('album', album_id=album_id)

    if request.method == "POST" and 'download_video' in request.POST:
        id = request.POST.get("download_video")
        video = Video.objects.get(id=id)
        return FileResponse(video.url_to_file, as_attachment=True)

    if request.method == "POST" and 'download_photo' in request.POST:
        id = request.POST.get("download_photo")
        img = Image.objects.get(id=id)
        return FileResponse(img.url_to_file.open(), as_attachment=True)


    return render(request, template_name, {
        "name": name,
        "videos": videos,
        "menu": Menu,
        "images": images,
        "users": users,
        "participants_ids": participants,
        "user_id": user_id,
        "form_image": form_image,
        "form_video": form_video,
        "album_id": album_id
    })


@login_required
def upload_image(request):
    template_name = "app/upload.html"
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                img = form.save(commit=False)
                img.user_id = request.user.id
                img.save()
                id = 0
                for image in Image.objects.filter(id=request.user.id):
                    if image.id > id:
                        id = image.id
                image = get_object_or_404(Album, id=id)

                return redirect('upload_image')
            except:
                form.add_error(None, "Ошибка загрузки")
    else:
        form = UploadImageForm()
    return render(request, template_name, {
        "form": form,
        "menu": Menu,
        "url": "upload_image"
    })


@login_required
def upload_video(request):
    template_name = "app/upload.html"
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                vid = form.save(commit=False)
                vid.user_id = request.user.id
                vid.save()
                return redirect('upload_video')
            except:
                form.add_error(None, "Ошибка загрузки")
    else:
        form = UploadVideoForm()
    return render(request, template_name, {
        "form": form,
        "menu": Menu,
        "url": "upload_video"
    })

@login_required
def show_profile(request, profile_id):
    user = get_object_or_404(User, id=profile_id)
    images = Image.objects.filter(user_id=profile_id)
    images_new = []
    videos = Video.objects.filter(user_id=profile_id)
    videos_new = []
    alb = Album.objects.filter(participant_ids__contains=str(profile_id))
    flag_img = True
    for image in images:
        for album in alb:
            if str(image.id) in album.image_ids.split(' '):
                flag_img = False
        if flag_img:
            images_new.append(image)
        flag_img = True

    flag_vid = True
    for video in videos:
        for album in alb:
            if str(video.id) in album.video_ids.split(' '):
                flag_vid = False
        if flag_vid:
            videos_new.append(video)
        flag_vid = True

    if request.method == 'POST' and request.user.id == profile_id:
        name = request.POST.get('name')
        Album.objects.create(participant_ids=str(request.user.id), image_ids='', video_ids='', name=name)
        return redirect('show_profile')

    return render(request, "app/profile.html", {
        "images": images_new,
        "videos": videos_new,
        "albums": alb,
        "profile_id": profile_id,
    })

def register(request):
    """
    Args:
        request:

    Returns:
        registration.html
    """
    template_name = 'app/registration.html'
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return redirect('login')
    else:
        user_form = RegistrationForm()
    return render(request, template_name, {
        'user_form': user_form
                   })

def login_view(request):
    """
    Args:
        request:

    Returns:
        login.html
    """
    template_name = 'app/login.html'
    form = LoginForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show_profile', user.id)
        else:
            error_message = 'Неверные учетные данные. Попробуйте еще раз.'
    else:
        error_message = ''
    return render(request, template_name, {
        'form': form, 'error_message': error_message
    })

def logout_view(request):
    """
    Args:
        request:

    Returns:
        logout to login.html
    """
    logout(request)
    return redirect('login')

def profile_search(request):
    model = User
    template_name = 'app/profile_search.html'
    users = model.objects.all()
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    users = model.objects.filter(username__iregex=q)
    return render(request, template_name, {
        'users': users,
    })