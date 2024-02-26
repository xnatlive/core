from django.forms import ModelForm
from django import forms

from customers.models import Company , Customer


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields =['name','nID','ceoName','career','mobile', 'tel','address','note']

        labels = { 
            'name': 'نام شرکت ',
            'ceoName': 'نام مدیر عامل',
            'nID':'شناسه شرکت',
            'career': 'حوضه فعالیت',
            'mobile': 'شماره موبایل',
            'tel': 'تلفن',
            'address': 'آدرس',
            'note': 'توضیحات',
        }
        widgets = {
            'name': forms.TextInput(attrs= {'class':'form-control'}),
            'ceoName': forms.TextInput(attrs= {'class':'form-control'}),
            'nID': forms.NumberInput(attrs= {'class':'form-control'}),
            'career': forms.TextInput(attrs= {'class':'form-control'}),
            'mobile': forms.NumberInput(attrs= {'class':'form-control'}),
            'tel': forms.NumberInput(attrs= {'class':'form-control'}),
            'address': forms.Textarea(attrs= {'class':'form-control','cols':50,'rows':3}),
            'note': forms.Textarea(attrs= {'class':'form-control','cols': 50, 'rows': 2}),
        }
        help_texts = {
            'name': 'نام  را وارد کنید',
            'ceoName': 'نام مدیر عامل  را وارد کنید',
            'nID': 'شناسه ملی را وارد کنید',   
            'career': 'حوضه فعالیت  را وارد کنید',
            'mobile': 'شماره موبایل  را وارد کنید',
            'tel': 'تلفن  را وارد کنید',
            'address': 'آدرس  را وارد کنید',
            'note': 'توضیحات  را وارد کنید',
            
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
            'name': 'نام  را وارد کنید',
            'family': 'نام خانوادگی  را وارد کنید',
            'nID': 'کد ملی  را وارد کنید',   
            'career': 'حوضه فعالیت  را وارد کنید',
            'mobile': 'شماره موبایل  را وارد کنید',
            'tel': 'تلفن  را وارد کنید',
            'address': 'آدرس  را وارد کنید',
            'note': 'توضیحات  را وارد کنید',
            
        }
        
    

        
        
