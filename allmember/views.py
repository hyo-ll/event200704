from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant
from .forms import AllmemberForm

# def index(request):
#     params = {
#         'title':'参加登録ページ',
#         'message':'名前',
#         'form':KobetsuForm(),
#         'goto':'next',
#         }
#     if (request.method == 'POST'):
#         params['message'] = '名前：' + request.POST['name'] + \
#             '<br>メール：' + request.POST['mail'] + \
#             '<br>年齢：' + request.POST['age']
#     params['form'] = KobetsuForm(request.POST)
#     return render(request, 'kobetsu/index.html', params)

def index(request):
    data = Participant.objects.all()
    params = {
        'title':'参加登録ページ',
        'message':'参加者リスト',
        'data':data,
        'goto':'next',
        }
    return render(request, 'allmember/index.html', params)

def next(request):
    params = {
        'title':'確認ページ',
        'msg':'2ページ目',
        'goto':'index',
        }
    return render(request, 'allmember/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'登録完了',
        'msg':'こんにちは、'+ msg + 'さん。',
        'goto':'index',
        }
    return render(request, 'allmember/index.html', params)
