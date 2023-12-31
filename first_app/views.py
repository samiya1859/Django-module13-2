from django.shortcuts import render,redirect

from . forms import contactform,StudentData,passwordValidation
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):

    if request.method == 'POST':
        print(request.POST)
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'about.html', {'name':name,'email':email,'select':select})
    else:
        return redirect(request,'about.html')

def submit_form(request):
    # print(request.POST)
    
    return render(request,'form.html')

from django.shortcuts import render, redirect

def DjangoForm(request):
    if request.method == 'POST':
        form = contactform(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'djangoform.html', {'form': form})
    else:
        form = contactform()

    return render(request, 'djangoform.html', {'form': form})


def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = StudentData()
        return render(request,'djangoform.html',{'form':form})
    
def PasswordValidation(request):
    if request.method == 'POST':
        form = passwordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = passwordValidation()
        return render(request,'djangoform.html',{'form':form})