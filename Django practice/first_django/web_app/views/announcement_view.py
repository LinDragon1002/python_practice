from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from web_app.models.announcement import Announcement
from web_app.forms.announcement_form import AnnouncementForm

def announcement_create(request):
    form = AnnouncementForm()
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'announcement/create.html', {"msg": "新增成功"})
    return render(request, 'announcement/create.html',{"form":form})

def announcement_update(request,id):
    announcement = get_object_or_404(Announcement, pk=id)
    form = AnnouncementForm(instance=announcement)
    data = {}
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            data['msg'] = "更改成功"
    data['form'] = form
            # return render(request, 'announcement/update.html', {"msg": "新增成功","form":form})
    return render(request, 'announcement/update.html',data)