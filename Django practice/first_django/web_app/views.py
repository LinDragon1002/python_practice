from django.http import HttpResponse
from django.shortcuts import render
from web_app.models import people

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

def register(request):
    data = {
        'gender_choices': people.gender_choices
    }
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        gender = request.POST['gender']
        age = request.POST['age']

        people.objects.create(
            name=name,
            phone=phone,
            gender=gender,
            age=age
        )
        data['msg'] = "新增成功"

    return render(request,"register.html",data)