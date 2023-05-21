from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('work', allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            userid = request.user.user.id
            print(userid)
            if group == allowed_roles[0] :
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        elif request.user.is_anonymous:
            return redirect("login")
        else:
            return redirect("user/"+str(request.user.users.id))
    return wrapper_func
   
