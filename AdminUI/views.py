from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Video
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    if request.user.is_authenticated:
        vids = Video.objects.all()
        return render(request,'index.html',{'vids':vids})
        # page = request.GET.get('page', 1)

        # paginator = Paginator(vids, 3)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users = paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)

        # return render(request, 'index.html', { 'vids': vids })
    res = render(request,'login.html',{'msg':'You need to login First!'})
    return res

def login_view(request):
    if request.POST:
        username = request.POST['user_id']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                vids = Video.objects.all()
                res = render(request,'index.html',{'msg':'Login Succesfull!','vids':vids})
                return res
        else:
            res = redirect(request,'login.html',{'msg':'Incorrect UserID or Password'})
            return res
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    res = render(request,'login.html',{'msg':'You have been Logged out'})
    return res

def add_video(request):
    if request.user.is_authenticated:
        if(request.POST):
            v_title = request.POST['v_title']
            v_url = request.POST['v_url']
            v_ft_model = request.POST['v_ft_model']
            nv = Video.objects.create(title=v_title,url=v_url,featuring=v_ft_model,category='Default Category')
            nv.save()
            vids = Video.objects.all()
            res = render(request,'index.html',{'msg':'Video Added','vids':vids})
            return res
    return redirect('/')