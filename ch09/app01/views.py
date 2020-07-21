from django.shortcuts import render, HttpResponse

from app01.forms.login import LoginForm


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            user_color = request.POST.get('user_color')
            # print(username)
            # print(user_color)
            message = '登录成功'
            response = HttpResponse(message)
            try:
                if username:
                    response.set_cookie('username', username)
                if user_color:
                    response.set_cookie('usercolor', user_color.encode('utf-8'))
            except:
                pass
            return response
        else:
            return render(request, 'app01/login.html', {'login_form': login_form})
    login_form = LoginForm()
    username = request.COOKIES.get('username')
    return render(request, 'app01/login.html', {'login_form': login_form, 'username': username})
