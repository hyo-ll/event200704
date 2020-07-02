from django import forms

class KobetsuForm(forms.Form):
    name = forms.CharField(label='名前(必須)')
    mail = forms.CharField(label='メールアドレス', required=False)
    ticket_number = forms.CharField(label='チケット番号', required=False)
#    admission_number = forms.CharField(label='admission_number', required=False)
    member_list=[
        ('神楽 美佳','神楽 美佳'),
        ('小松 かやの','小松 かやの'),
        ('椎葉 彩','椎葉 彩'),
        ('成沢 くれは','成沢 くれは'),
        ('花ノ宮 あみな','花ノ宮 あみな'),
        ('海月 るり','海月 るり'),
        ('宮原 愛葵','宮原 愛葵'),
        ]
    choice_member = forms.ChoiceField(label='希望メンバー(必須)', \
                                      choices=member_list)
