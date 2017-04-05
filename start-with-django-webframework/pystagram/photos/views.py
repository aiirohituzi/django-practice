from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
from .forms import PhotoForm
from django.shortcuts import redirect

# from django.conf import settings
from django.contrib.auth.decorators import login_required

def hello(request):
    return HttpResponse('안녕하세요!')

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))

@login_required
def create(request):
    # if not request.user.is_authenticated():
    #     return redirect(settings.LOGIN_URL)

    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)      # true일 경우 바로 데이터베이스에 적용, 현재 유저정보가 담기지 않았기에 not null 제약조건에 걸려 작업이 실패하므로 false
            obj.user = request.user
            obj.save()      # obj.save(commit=True) 와 동일

            return redirect(obj)


    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)