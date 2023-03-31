from django.shortcuts import redirect


def index(request):
    # return redirect('accountbooks:index')   # urls 경로 지정 수 수정
    return redirect('account-book/')


