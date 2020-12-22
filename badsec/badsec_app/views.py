from django.contrib.auth.models import User
from django.db.models import query
from django.shortcuts import redirect, render
from .models import Account
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.db import connection

# Create your views here.


def index(request):
    return render(request, 'badsec_app/index.html')


def accounts(request):
    if request.method == 'POST':
        owner_id = User.objects.get(username=request.user).id

        query = "INSERT INTO badsec_app_account (owner_id, balance, iban) VALUES (" + str(owner_id) + ", 500, '%s')" % request.POST.get('iban')

        print(query)
        res=connection.cursor().execute(query)

    accounts=Account.objects.filter(owner=request.user)
    return render(request, 'badsec_app/accounts.html', {'accounts': accounts})


def account(request):
    if request.method == 'POST':
        sender=request.POST.get('from')
        receiver=request.POST.get('to')
        amount=int(request.POST.get('amount'))

        transfer(sender, receiver, amount)

    userAccount=Account.objects.get(pk=request.GET.get('account'))
    accounts=Account.objects.exclude(pk=request.GET.get('account'))
    return render(request, 'badsec_app/account.html', {'userAccount': userAccount, 'accounts': accounts})


def amount_is_valid(balance, amount):
    if amount < 0 or balance < amount:
        return False
    return True


def transfer(sender, receiver, amount):
    acc1=Account.objects.get(iban=sender)
    acc2=Account.objects.get(iban=receiver)

    if amount_is_valid(acc1.balance, amount):
        acc1.balance -= amount
        acc2.balance += amount

        acc1.save()
        acc2.save()


def sign_up(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/login/')
    else:
        form=SignUpForm()
    return render(request, 'badsec_app/signup.html', {'form': form})
