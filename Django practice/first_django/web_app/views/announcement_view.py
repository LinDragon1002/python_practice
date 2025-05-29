from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from web_app.models.announcement import Announcement
from web_app.forms.announcement_form import AnnouncementForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q


def announcement_list(request):
    if request.user.is_authenticated:
        datas = Announcement.objects.all()
        return render(request,'announcement/admin.html',{'datas':datas})
    else:
        now = timezone.now()
        datas = Announcement.objects.filter(
            Q(start_time__lte=now) | Q(start_time__isnull=True),
            Q(end_time__gte=now) | Q(end_time__isnull=True))
        return render(request,'announcement/list.html',{'datas':datas})

@login_required
def announcement_delete(request, id):
    announcement = get_object_or_404(Announcement, pk=id)
    announcement.delete()
    return redirect('announcement_list')

@login_required
def announcement_create(request):
    form = AnnouncementForm()
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'announcement/create.html', {"msg": "新增成功"})
            return redirect('announcement_list')
    return render(request, 'announcement/create.html',{"form":form})

@login_required
def announcement_update(request,id):
    announcement = get_object_or_404(Announcement, pk=id)
    form = AnnouncementForm(instance=announcement)
    data = {}
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            data['msg'] = "更改成功"
            return redirect('announcement_list')
    data['form'] = form
            # return render(request, 'announcement/update.html', {"msg": "新增成功","form":form})
    return render(request, 'announcement/update.html',data)
