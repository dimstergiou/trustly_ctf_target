from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from levels.forms import LoginForm, BestCompany, CreditCard
from .utils import valid_credentials
from .models import Content
import pycard

def index(request):
    return render(request, "index.html", {})

# def indexDemo(request):
#     return render(request, "index2.html", {})

def level1(request):
    return render(request, "levels/l1.html", {'level': reverse('levels:l1')})

def level2(request):
    return render(request, "levels/l2.html", {'level': reverse('levels:l2')})

def level4(request):
    response = render(request, "levels/l4.html", {'level': reverse('levels:l4')})
    response.set_cookie(key='flag', value='flag{hungry}', path=request.path)
    return response

def level7(request):
    response = render(request, "levels/l7.html", {'level': reverse('levels:l7')})
    response['here_is_the_flag'] = 'flag{dimitrios}'
    return response

def level9(request):
    error = None
    success = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if valid_credentials(username,password):
                success = 'Correct: The flag is: flag{lego}'
            else:
                error = 'Error: Invalid login'
    else:
        form = LoginForm()
    context = {
        'level': reverse('levels:l9'),
        'form': form,
        'error': error,
        'success': success,
    }
    return render(request, "levels/l9.html", context)

def level12(request):
    return render(request, "levels/l12.html", {'level': reverse('levels:l12')})

def level13(request):
    return render(request, "levels/l13.html", {'level': 13})

def level13_flag(request):
    return HttpResponse('flag{tdd}')

def level15(request):
    error = None
    success = None
    result = None
    if request.method == 'POST':
        input = request.POST.get('input')
        query = "SELECT * from levels_content WHERE name = '%s'" % input
        result = Content.objects.raw(query)
        if result:
            success = True
            result = result
        else:
            error = '0 results found!'

    context = {
        'level': reverse('levels:l15'),
        'error': error,
        'success': success,
        'result' : result
    }
    return render(request, "levels/l15.html", context)

def level16(request):
    return render(request, "levels/l16.html", {'level': reverse('levels:l16')})

def level17(request):
    return render(request, "levels/l17.html", {'level': reverse('levels:l17')})

def level19(request):
    error = None
    success = None
    if request.method == 'POST':
        form = BestCompany(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company'].lower()
            if company == "trustly":
                success = 'Correct: The flag is: flag{oscar}'
            else:
                error = 'Error: Not the answer we are looking for'
    else:
        form = BestCompany()
    context = {
        'level': reverse('levels:l19'),
        'form': form,
        'error': error,
        'success': success,
    }
    return render(request, "levels/l19.html", context)

def level20(request):
    return render(request, "levels/l20.html", {'level': reverse('levels:l20')})

def level22(request):
    response = render(request, "levels/l22.html", {'level':reverse('levels:l22')})
    secret = request.headers.get('Secret')
    if str(secret).lower() == 'innovation':
        response['here_is_the_flag'] = 'flag{awesome}'
    return response

def level23(request):
    return render(request, "levels/l23.html", {'level': reverse('levels:l23')})

def level23_robots(request):
    return HttpResponse('User-Agent: *\nDisallow /aa2646a667ee1cd83235786dccef4a26/', content_type='text/plain')

def level23_flag(request):
    return HttpResponse('flag{ultron}')

def level24(request):
    if request.user_agent.is_mobile:
        return HttpResponse('flag{anna}')
    else:
        return render(request, "levels/l24.html", {'level': reverse('levels:l24')})

def level25(request):
    error = None
    success = None
    if request.method == 'POST':
        form = CreditCard(request.POST)
        if form.is_valid():
            card = form.cleaned_data['card']
            cc = pycard.Card(number=card, month=1, year=2020, cvc=123)
            if cc.is_valid:
                success = 'Correct: The flag is: flag{money}'
            else:
                error = 'Not a valid credit card'
    else:
        form = CreditCard()
    context = {
        'level': reverse('levels:l25'),
        'form': form,
        'error': error,
        'success': success,
    }
    return render(request, "levels/l25.html", context)

def level26(request):
    error = None
    success = None
    if request.method == 'POST':
        if request.user_agent.is_bot:
            success = 'flag{bing}'
        else:
            error = 'You are not Google. User agent: ' + str(request.user_agent)

    context = {
        'level': reverse('levels:l26'),
        'error': error,
        'success': success,
    }
    return render(request, "levels/l26.html", context)

def level27(request):
    success = None
    context = {
        'level': reverse('levels:l27'),
        'success': success,
    }
    flag_value = request.COOKIES.get('flag')
    response = render(request, "levels/l27.html", context)
    if 'flag' not in request.COOKIES:
        response.set_cookie(key='flag', value='0', path=request.path)
    if flag_value == '1':
        print(flag_value)
        context['success'] = 'flag{john}'
        return render(request, "levels/l27.html", context)
    return response

def level29(request):
    success = None
    error = None
    ip = request.headers.get('X-FORWARDED-FOR')
    if ip == "1.1.1.1":
        success = "flag{dorna}"
    else:
        error = "This site is only accessible from 1.1.1.1"
    context = {
        'level': reverse('levels:l29'),
        'success': success,
        'error': error,
    }
    return render(request, "levels/l29.html", context)

def level30(request):
    error = None
    # if request.method == "GET" or request.method == "POST":
    #     error = "You have failed to delete the /supersecret.txt file"
    # if request.method == "DELETE":
    #     success = "File deleted - flag{swtor}"
    context = {
        'level': reverse('levels:l30'),
        'error': error,
    }
    return render(request, "levels/l30.html", context)

@csrf_exempt
def level30_d(request):
    if request.method == "DELETE":
        return HttpResponse('File deleted - flag{swtor}')
    else:
        return HttpResponse('Nothing to see here')

def level34(request):
    # wscat -c ws://trustlyctf.herokuapp.com/flag
    return render(request, "levels/l34.html", {'level': reverse('levels:l34')})
