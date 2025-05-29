from django.contrib import auth
from django.shortcuts import redirect,render

def login(request):
    error = None
    if request.user.is_authenticated:
        return redirect('announcement_list')
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is None:
            error = "用戶名稱或密碼錯誤"
        else:
            auth.login(request, user)
            return redirect('announcement_list')
    return render(request,'login/login.html', {'error': error})

def logout(request):
    auth.logout(request)
    return redirect('login')
