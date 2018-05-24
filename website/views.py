from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseForbidden, JsonResponse, Http404,HttpResponseRedirect

from .tokens import account_activation_token 
from .email import send_confirmation_email
from .forms import SignUpForm


from .models import Foods
from .forms import FoodsForm

# Create your views here.

def index(request):
    item = Foods.objects.all()
    context = {'foods':item}
    return render(request, "home.html",context)

def booktable(request):
	context = {}
	return render(request, "booktable.html",context)

def profile(request):
    item = Foods.objects.all()
    context = {'foods':item}

    return render(request, "profile.html",context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            current_site = get_current_site(request)
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            pwd_hash = make_password(raw_password)

            #Save to User table
            new_user = User(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd_hash)
            if not User.objects.filter(username=username).exists():
                new_user.is_active = False
                new_user.save()

                send_confirmation_email(new_user, current_site, email)
                messages.success(request, 'Congratulations! Email has been sent to your provided email account for confirmation!')
                return redirect('login')
            else:
                messages.info(request, "Username taken!")
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for confirming your email address!')
        return redirect('login')

    else:
        messages.error(request, 'OHH NO! The confirmation link is invalid or has expired.')
        return redirect('login')


def contactus(request):
	context = {}
	return render(request, "contactus.html",context)

def menus(request):
	context = {}
	return render(request, "menu.html",context)


def food_form_view(request):

    if request.method == "POST":
        form = FoodsForm(request.POST)
        if form.is_valid():
            dic = form.cleaned_data

            menus = Foods(**dic)
            menus.save()


            form = FoodsForm()
            context = {"form":form}
            return render(request, "menu_form.html",context)
    else:
        form = FoodsForm()
        context = {
            "form":form,
            "form_action": "/menuform/"
        }
        return render(request, "menu_form.html",context)

def food_form_edit(request,id):

    try:
        item = Foods.objects.get(pk=id)
        form = FoodsForm(
            initial={
                'fname': item.fname,
                'desc': item.desc,
                'other_info': item.other_info,
                'category': item.category,
                'price_s': item.price_s,
                'price_m': item.price_m,
                'price_l': item.price_l,
                'price': item.price,
                'f_status': item.f_status,
            }
        )

        context = {
            "form":form,
            "form_action": "/menuedit/"+id+"/"
        }

    except (ObjectDoesNotExist, Foods.DoesNotExist):
        raise Http404("Product does not exist")
    else:
        if request.method == 'POST':

            form = FoodsForm(request.POST)
            if form.is_valid():
                dic = form.cleaned_data

                menus = Foods.objects.filter(pk=id).update(**dic)

                return HttpResponseRedirect("/menuedit/"+id+"/")

        else:

            return render(request, "menu_form.html",context)

        