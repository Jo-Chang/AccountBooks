from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.
def index(request):
    accountbooks = AccountBook.objects.all()
    
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    print(accountbook.__dict__)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    account = AccountBook()
    g = request.POST.get
    account.note = g('note')
    account.description = g('description')
    account.category = g('category')
    account.amount = g('amount')
    account.date = g('date')
    account.save()
    # account.date가 빈 값인지 체크
    # 빈 값이라면 -> new (X)

    return redirect('account-book:index')