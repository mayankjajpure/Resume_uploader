from django.shortcuts import render
from .forms import resumeform
from .models import resume
from django.views import View

# Create your views here.

class Homeview(View):
    def get(self,request):
        form=resumeform()
        candidates=resume.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})


    def post(self,request):
        form=resumeform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'myapp/home.html',{'form':form})

class candidate_view(View):
    def get(self,request,pk):
        print(pk)
        candidate=resume.objects.get(pk=pk)
        return render(request,'myapp/detail.html',{'candidate':candidate})