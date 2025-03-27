from django.http import HttpResponse
from django.shortcuts import render

user_data = []
# Create your views here.
def view_main(request):
    name = "林原郁"
    return HttpResponse(f"<p>hello {name}</p>")

def view_register(request):
    username = request.POST.get("user_name")
    userpassword = request.POST.get("user_password")
    if username and userpassword:
        user_data.append([username,userpassword])
    return render(request,'index.html',{"datas": user_data})