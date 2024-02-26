from django.shortcuts import render,redirect
from customers.models import Customer , Company
from customers.forms   import CustomerForm , CompanyForm

from django.core.paginator import Paginator
from django.db.models import Q 
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.





# Create your views here.
#@login_required
def customers_view(request):
    customers = Customer.objects.all()

    search = request.GET.get('search')
    if search:
        customers = customers.filter(Q(name__icontains=search)|Q(family__icontains=search)|Q(mobile__icontains=search))
    paginator = Paginator(customers, 10) # Show 10 customers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'customers/customers.html', context)
    

def view_customer(request, id):
    customer = Customer.objects.get(pk=id)
    return HttpReponseReirect(reverse('customers'))

def edit_customer(request, id):

    if request.method == 'POST':

        customer = Customer.objects.get(pk=id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return render(request,'customers/edit_customer.html',{
                'form': form,
                'success': True
            
            })

    
    else:
        customer = Customer.objects.get(pk=id)
        form = CustomerForm(instance=customer)


    return render (request,'customers/edit_customer.html',{
        'form': form
    })




def add_customer(request):
    if request.method == 'POST':
        # Create form and validate data
        form = CustomerForm(request.POST) 
        if form.is_valid():
            new_customer_name = form.cleaned_data['name']
            new_customer_family = form.cleaned_data['family']
            new_customer_nID = form.cleaned_data['nID']
            new_customer_career = form.cleaned_data['career']
            new_customer_mobile = form.cleaned_data['mobile']
            new_customer_tel = form.cleaned_data['tel']
            new_customer_address = form.cleaned_data['address']
            new_customer_note = form.cleaned_data['note']

            new_customer = Customer(
                name=new_customer_name,
                family=new_customer_family,
                nID=new_customer_nID,
                career=new_customer_career,
                mobile=new_customer_mobile,
                tel=new_customer_tel,
                address=new_customer_address,
                note=new_customer_note)
            new_customer.save()


            #form.save()
            return render(request, 'customers/add_customer.html', {'form': form , 'success': True})
    else:
        form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})


def delete_customer(request, id):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=id)
        customer.delete()
    return HttpResponseRedirect(reverse('customers'))


###


#-----------    Company
def companies_view(request):
    companies = Company.objects.all()

    search = request.GET.get('search')
    if search:
        companies = companies.filter(Q(name__icontains=search)|Q(family__icontains=search)|Q(mobile__icontains=search))

    paginator = Paginator(companies, 10) # Show 10 customers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'companies/companies.html', context)
    
def view_company(request, id):
    company = Company.objects.get(pk=id)
    return HttpReponseReirect(reverse('companies'))


def edit_company(request, id):

    if request.method == 'POST':

        company = Company.objects.get(pk=id)
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return render(request,'companies/edit_company.html',{
                'form': form,
                'success': True
            
            })

    
    else:
        company = Company.objects.get(pk=id)
        form = CompanyForm(instance=company)


    return render (request,'companies/edit_company.html',{
        'form': form
    })




def add_company(request):
    if request.method == 'POST':
        # Create form and validate data
        form = CompanyForm(request.POST) 
        if form.is_valid():
            new_customer_name = form.cleaned_data['name']
            new_customer_ceoName = form.cleaned_data['ceoName']
            new_customer_nID = form.cleaned_data['nID']
            new_customer_career = form.cleaned_data['career']
            new_customer_mobile = form.cleaned_data['mobile']
            new_customer_tel = form.cleaned_data['tel']
            new_customer_address = form.cleaned_data['address']
            new_customer_note = form.cleaned_data['note']

            new_customer = Company(
                name=new_customer_name,
                ceoName=new_customer_ceoName,
                nID=new_customer_nID,
                career=new_customer_career,
                mobile=new_customer_mobile,
                tel=new_customer_tel,
                address=new_customer_address,
                note=new_customer_note)
            new_customer.save()


            #form.save()
            return render(request, 'companies/add_company.html', {'form': form , 'success': True})
    else:
        form = CompanyForm()
    return render(request, 'companies/add_company.html', {'form': form})


def delete_company(request, id):
    if request.method == 'POST':
        company = Company.objects.get(pk=id)
        company.delete()
    return HttpResponseRedirect(reverse('companies'))




