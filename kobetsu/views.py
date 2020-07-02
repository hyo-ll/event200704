from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Max
from .models import Participant
from .forms import KobetsuForm
import urllib.parse

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
        'data':data,
        'goto':'next',
        }
    return render(request, 'kobetsu/index.html', params)

def participate(request):
    params = {
        'title':'参加登録ページ',
        'form':KobetsuForm(),
        }
    if (request.method == 'POST'):
        
        #idの設定
        if Participant.objects.all().first() is None:
            admission_number = 20200702001; #一番最初の人処理
        else:
            max_id = Participant.objects.all().aggregate(Max('id')) #最大値を取得
            max_id_value = list(max_id.values()) #辞書型の値を取得してint型に直す
            id = max_id_value[0] + 1
        
        #名前,メールアドレス,チケット番号,希望メンバーの設定
        name = request.POST['name']
        mail = request.POST['mail']
        ticket_number = request.POST['ticket_number']
        choice_member = request.POST['choice_member']
        
        #整理番号の発行
        querySet = Participant.objects.filter(choice_member=choice_member)
        if querySet.first() is None:
            admission_number = 1; #一番最初の人処理
        else:
            max_admission_number = querySet.aggregate(Max('admission_number')) #最大値を取得
            max_admission_value = list(max_admission_number.values()) #辞書型の値を取得してint型に直す
            admission_number = max_admission_value[0] + 1 #整理番号の発行
            
        #データの書き込み
        participant = Participant(id=id,name=name,mail=mail,ticket_number=ticket_number,\
                                  admission_number=admission_number,choice_member=choice_member)
        participant.save()
        
        #セッションの保存
        request.session['id'] = id
        return redirect(to='/kobetsu/wait')
    return render(request, 'kobetsu/participate.html', params)

def wait(request):
    session_id = request.session['id']
    data = Participant.objects.get(id=session_id)
    params = {
        'title':'受付完了',
        'data':data,
        # 'name':data[1],
        # 'admission_number':data[4],
        # 'choice_member':data[5],
        }
    return render(request, 'kobetsu/wait.html', params)

def next(request):
    params = {
        'title':'確認ページ',
        'msg':'2ページ目',
        'goto':'index',
        }
    return render(request, 'kobetsu/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'登録完了',
        'msg':'こんにちは、'+ msg + 'さん。',
        'goto':'index',
        }
    return render(request, 'kobetsu/index.html', params)
