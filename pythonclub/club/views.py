from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'club/index.html') 



def getresource(request):
    re_source= Resource.objects.all()
    return render(request,'club/source.html', {'re_source': re_source} )

def getmeeting(request):
    meet= Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meet': meet})

def meetid(request, id):
     details= get_object_or_404(Meeting.objects, id=id)
     return render(request, 'club/meetdetails.html', {'details':details})

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method== 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    Reform=ResourceForm
    if request.method== 'POST':
        Reform=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            Reform=ResourceForm()
    else:
        Reform=ResourceForm()
    return render(request, 'club/newresource.html', {'Reform': Reform})


def loginmessage(request):
    return render(request, 'club/loginmesage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')
