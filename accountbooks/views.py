from django.shortcuts import render, redirect
from datetime import datetime
from .models import AccountBook

# Create your views here.
def index(request):
    accountbooks = AccountBook.objects.all()
    
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, pk: int):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    account = AccountBook()
    g = request.POST.get
    account.note = g('note') if g('note') else '미정'
    account.category = g('category') if g('category') else '미정'
    account.date = g('date') if g('date') else datetime.today().strftime('%Y-%m-%d')
    account.description = g('description')
    account.amount = g('amount')
    # 기타 유효성 체크 코드
    # ...
    # account.date가 빈 값인지 체크
    # 빈 값이라면 -> new (X)
    # if not account.date:   # 아직 빈 값
    # if not g('date'):
    #     # 에러 페이지로 redirect
    #     return redirect('account-books:new')
    account.save()
    
    return redirect('account-books:index')


def delete (_, pk):
    g = AccountBook.objects.get(pk=pk)
    g.delete()
    
    return redirect('account-books:index')


def copy(_, pk):
    account = AccountBook.objects.get(pk=pk)
    account.pk = None
    account.save()
    
    return redirect('account-books:index')


def edit(request, pk):
    account = AccountBook.objects.get(pk=pk)
    context = {
        'data': account,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, pk):
    account = AccountBook(pk=pk)
    g = request.POST.get
    account.note = g('note') if g('note') else '미정'
    account.category = g('category') if g('category') else '미정'
    account.date = g('date') if g('date') else datetime.today().strftime('%Y-%m-%d')
    account.description = g('description')
    account.amount = g('amount')
    account.save()
    
    return redirect('account-books:detail', account.pk)