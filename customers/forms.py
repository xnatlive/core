from django.forms import ModelForm
from django import forms

from customers.models import Company , Customer


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields =['name','nID','ceoName','career','mobile', 'tel','address','note']
        widget = forms.TextInput(
            attrs= {
                'class': 'form-control',
            }
        )
        labels = { 
            'name': 'نام شرکت '
        }

    


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields =['name','family','nID','career','mobile', 'tel','address','note']
        labels = { 
            'name': 'نام',
            'family':'نام خانوادگی',
            'nID': 'کد ملی',
            'career': 'حوضه فعالیت',
            'mobile': 'شماره موبایل',
            'tel': 'تلفن',
            'address': 'آدرس',
            'note': 'توضیحات'
        }
        widgets = {
            'name': forms.TextInput(attrs= {'class':'form-control'}),
            'family': forms.TextInput(attrs= {'class':'form-control'}),
            'nID': forms.NumberInput(attrs= {'class':'form-control'}),
            'career': forms.TextInput(attrs= {'class':'form-control'}),
            'mobile': forms.NumberInput(attrs= {'class':'form-control'}),
            'tel': forms.NumberInput(attrs= {'class':'form-control'}),
            'address': forms.Textarea(attrs= {'class':'form-control','cols':50,'rows':3}),
            'note': forms.Textarea(attrs= {'class':'form-control','cols': 50, 'rows': 2}),
        }
        help_texts = {
            'name': 'نام خود را وارد کنید',
            'family': 'نام خانوادگی خود را وارد کنید',
            'nID': 'کد ملی خود را وارد کنید',   
            'career': 'حوضه فعالیت خود را وارد کنید',
            'mobile': 'شماره موبایل خود را وارد کنید',
            'tel': 'تلفن خود را وارد کنید',
            'address': 'آدرس خود را وارد کنید',
            'note': 'توضیحات خود را وارد کنید',
            
        }
        
    

        
        
