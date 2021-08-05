from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import *

# def home(request):
#     user_id = request.session.get('user')
#     #print(user_id)
#     if user_id:
#         member = BoardMember.objects.get(pk=user_id)
#         return HttpResponse(member.username)

#     return HttpResponse('Home!')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        res_data ={}

        if not (email and password):
            res_data['error'] = '모든 값을 입력하세요!'

        else:
            member = BoardMember.objects.get(email=email)
            #print(member.id)

            if check_password(password, member.password):
                request.session['user'] = member.id
                return redirect('/')

            else:
                res_data['error'] = '비밀번호가 일치하지 않습니다.'

        return render(request, 'login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        #print (request.POST)
        username    = request.POST.get('username', None)
        #print(username)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        email       = request.POST.get('email', None)
        nickname    = request.POST.get('nickname', None)
        res_data = {}

        if BoardMember.objects.filter(nickname=request.POST['nickname']).exists():
            res_data['error'] = '이미 존재하는 별명입니다.'
            print(res_data)
        
        if BoardMember.objects.filter(email=request.POST['email']).exists():
            res_data['error'] = '이미 존재하는 이메일입니다.'
            print(res_data)


        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            print(res_data)

        else:
            member = BoardMember(
                username    = username,
                nickname    = nickname,
                email       = email,
                password    = make_password(password)
            )
            member.save()

    return render(request, 'register.html', res_data)