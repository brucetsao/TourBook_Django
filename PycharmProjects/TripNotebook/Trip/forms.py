from django import forms
from .models import TripMain,Plan

class TripMainForm(forms. ModelForm):
    class Meta:
        model = TripMain
        fields = ['TripName','MainLocation','Description','DateStart','DateEnd','TopPhoto','TotalDay']
        labels = {
                     'TripName':'行程標題',
                     'MainLocation':'主要旅行地區（國家）',
                     'Description':'簡短描述',
                     'DateStart':'起始日期',
                     'DateEnd':'結束日期',
                     'TopPhoto':'圖片(完整網址)',
                     'TotalDay':'旅遊天數'

                  }
        help_texts = {
            'TopPhoto': '請貼上封面圖片的完整網址喔～',
            'DateStart': '範例格式：2016-04-27',
            'DateEnd': '範例格式：2016-04-27'
        }

        widgets = {
            'TripName': forms.TextInput(attrs={'style':'width:250px'}),
            'MainLocation': forms.TextInput(attrs={'style': 'width:250px'}),
            'Description': forms.TextInput(attrs={'style': 'width:500px'}),
            'DateStart': forms.TextInput(attrs={'style': 'width:100px'}),
            'DateEnd': forms.TextInput(attrs={'style': 'width:100px'}),
            'TopPhoto' : forms.TextInput(attrs={'style':'width:500px'}),
            'TotalDay': forms.TextInput(attrs={'style': 'width:100px'}),
        }

TYPE_CHOICES = (('景點','景點'),
                ('購物','購物'),
                ('住宿','住宿'),
                ('用餐','用餐'))

class PlanForm(forms. ModelForm):

    class Meta:
        model = Plan
        fields = ['PlanName','LocationName','Address','TimeStart','TimeEnd','Description','PhotoPath','dayCount','Type']
        labels = {
            'PlanName': '單一行程名稱',
            'LocationName': '地點名稱',
            'Address': '地址',
            'TimeStart': '起始日期時間',
            'TimeEnd': '結束日期時間',
            'Description': '行程敘述',
            'PhotoPath': '行程照片網址',
            'dayCount':'屬於第幾天的行程',
            'Type':'行程類型'
        }
        # mainTripId


        widgets = {
            'PlanName': forms.TextInput(attrs={'style': 'width:250px'}),
            'LocationName': forms.TextInput(attrs={'style': 'width:250px'}),
            'Address': forms.TextInput(attrs={'style': 'width:250px'}),
            'TimeStart': forms.TextInput(attrs={'style': 'width:100px'}),
            'TimeEnd': forms.TextInput(attrs={'style': 'width:100px'}),
            'Description': forms.TextInput(attrs={'style': 'width:500px'}),
            'PhotoPath': forms.TextInput(attrs={'style': 'width:500px'}),
            'dayCount': forms.TextInput(attrs={'style': 'width:100px'}),
        }