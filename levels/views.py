from django.shortcuts import render, HttpResponse
from django.urls import reverse
from levels.forms import LoginForm, BestCompany, CreditCard
from .utils import valid_credentials
from .models import Content
import pycard

def index(request):
    return render(request, "index.html", {})

def indexDemo(request):
    return render(request, "index2.html", {})

def level1(request):
    return render(request, "levels/l1.html", {'level':1})

def level2(request):
    return render(request, "levels/l2.html", {'level':2})

def level4(request):
    response = render(request, "levels/l4.html", {'level':4})
    response.set_cookie(key='flag', value='flag{hungry}', path=request.path)
    return response

def level7(request):
    response = render(request, "levels/l7.html", {'level': 7})
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
                error = None
            else:
                success = None
                error = 'Error: Invalid login'
    else:
        form = LoginForm()
    context = {
        'level': 9,
        'form': form,
        'error': error,
        'success': success,
    }
    return render(request, "levels/l9.html", context)

def level12(request):
    return render(request, "levels/l12.html", {'level':12})

def level13(request):
    return render(request, "levels/l13.html", {'level':13})

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
        'level': 15,
        'error': error,
        'success': success,
        'result' : result
    }
    return render(request, "levels/l15.html", context)

def level16(request):
    return render(request, "levels/l16.html", {'level':16})

def level17(request):
    return render(request, "levels/l17.html", {'level':17})

def level19(request):
    error = None
    success = None
    if request.method == 'POST':
        form = BestCompany(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company'].lower()
            if company == "trustly":
                success = 'Correct: The flag is: flag{oscar}'
                error = None
            else:
                success = None
                error = 'Error: Not the answer we are looking for'
    else:
        form = BestCompany()
    context = {
        'level': reverse('l9'),
        'form': form,
        'error': error,
        'success': success,
    }
    return render(request, "levels/l19.html", context)

def level20(request):
    return render(request, "levels/l20.html", {'level':20})

def level22(request):
    response = render(request, "levels/l22.html", {'level':22})
    secret = request.headers.get('Secret')
    if str(secret).lower() == 'innovation':
        response['here_is_the_flag'] = 'flag{awesome}'
    return response

def level23(request):
    return render(request, "levels/l23.html", {'level':23})

def level23_robots(request):
    return HttpResponse('flag{ultron}')

def level24(request):
    if request.user_agent.is_mobile:
        return HttpResponse('flag{anna}')
    else:
        return render(request, "levels/l24.html", {'level':24})

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
                error = None
            else:
                success = None
                error = 'Not a valid credit card'
    else:
        form = CreditCard()
    context = {
        'level': 25,
        'form': form,
        'error': error,
        'success': success,
    }
    return render(request, "levels/l25.html", context)