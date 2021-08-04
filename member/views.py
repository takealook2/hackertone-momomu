from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from .models import BoardMember

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        #print (request.POST)
        nickname    = request.POST.get('nickname', None)
        #print(nickname)
        username    = request.POST.get('username', None)
        #print(username)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        email       = request.POST.get('email', None)


        res_data = {}
        if  password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            print(res_data)

        else:
            member = BoardMember(
                username    = username,
                email       = email,
                password    = make_password(password),
                nickname    = nickname
            )
            member.save()

        return render(request, 'register.html', res_data)