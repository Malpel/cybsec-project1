from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Account

# Create your views here.
def index(request):
    return render(request, 'badsec_app/index.html')

def accounts(request):
	if request.method == 'POST':
		acc = Account(owner=request.user, iban=request.POST.get('iban'))
		acc.save()

	accounts = Account.objects.filter(owner=request.user)
	return render(request, 'badsec_app/accounts.html', { 'accounts': accounts })

def account(request):
	if request.method == 'POST':
		sender = request.POST.get('from')
		receiver = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		
		transfer(sender, receiver, amount)
	
	userAccount = Account.objects.filter(pk=request.GET.get('account'))
	accounts = Account.objects.exclude(owner=request.GET.get('user'))
	return render(request, 'badsec_app/account.html', { 'userAccount': userAccount, 'accounts': accounts })

def amount_is_valid(balance, amount):
	if amount < 0 or balance < amount:
		return False
	return True

def transfer(sender, receiver, amount):
	acc1 = Account.objects.get(iban=sender)
	acc2 = Account.objects.get(iban=receiver)

	if amount_is_valid(acc1.balance, amount):
		acc1.balance -= amount
		acc2.balance += amount

		acc1.save()
		acc2.save()