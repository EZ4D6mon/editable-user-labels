from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import TagForm, CreateUserForm, UsersForm
from .decorators import allowed_users, admin_only
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                #print("############registered success")
                user = form.save()
                #username = form.cleaned_data.get('username')
                Users.objects.create(
                    user=user,
                )

                return redirect('login')
            #

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@admin_only
def home(request):
    users = Users.objects.all()
    tags = Tag.objects.all()
    total_users = users.count()
    total_tags = tags.count()
    user = request.user.users
    #print('user=',user)
    return render(request, 'accounts/dashboard.html', {'users':users, 'total_users':total_users, 'total_tags':total_tags, 'user':user})

def about(request):
    user = request.user.users
    #form = UsersForm(instance=user)
    print('userid=',user.id)
    return render(request, 'accounts/about.html',{'user':user})

@login_required(login_url='login')
def userPage(request, pk_test):
    user = Users.objects.get(id = pk_test)
    temp = request.user.users
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    # print('userid=',user.id)
    # print('temp=', temp)
    tags = user.tag.all()
    return render(request, 'accounts/user.html', {'tags':tags, 'user':user, 'temp':temp, 'group':group})

def accountSettings(request):
    user = request.user.users
    form = UsersForm(instance=user)

    if request.method =='POST':
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login')
def createTag(request):
    user = request.user.users
    form = TagForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            user.tag.add(tag)
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/tag_form.html', context)

def renameTag(request, pk):
    item = Tag.objects.get(id = pk)
    form = TagForm(instance=item)
    if request.method == "POST":
        form = TagForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            #print("item=",item)
        #previous_page = request.META.get('HTTP_REFERER', '/')
            return redirect('home')
   
    context = {'form':form}
    
    return render(request, 'accounts/rename.html', context)

def deleteTag(request, pk):
    item = Tag.objects.get(id = pk)
    user = Users.objects.get(tag = item)
    
    if request.method == "POST":
        user.tag.remove(item)
        #print("item=",item)
        #previous_page = request.META.get('HTTP_REFERER', '/')
        return redirect('home')
   
    context = {'item':item}
    
    return render(request, 'accounts/delete.html', context)