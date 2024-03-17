from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render

from .forms import LoginForm


def staff_required(user):
    return user.is_authenticated and  user.is_staff


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('/admin')
    
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('/admin')
            elif user is not None and not user.is_staff:
                login(request, user)
                return redirect('/')
            else:
                msg= 'Invalid Credentials'
        else:
            msg = 'Invalid Form'

    return render(request, 'admin_login.html', {'form': form, 'msg': msg})


@user_passes_test(staff_required, login_url='/adminlogin')
def admin(request):
    return render(request,'admin.html')


def signout(request):
    if request.user.is_staff:
        url = "/admin"
    else:
        url = "/"
    logout(request)
    return redirect(url)

 