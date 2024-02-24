from django.shortcuts import render,redirect
from customers.models import Customer , Company
from customers.forms   import CustomerForm

from django.core.paginator import Paginator

# Create your views here.





# Create your views here.
#@login_required
def customers_view(request):
    customers = Customer.objects.all()

    search = request.GET.get('search')
    if search:
        customers = customers.filter(name__icontains=search)

    paginator = Paginator(customers, 10) # Show 10 customers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'customers.html', context)
    
def companies_view(request):
    companies = Company.objects.all()

    search = request.GET.get('search')
    if search:
        companies = companies.filter(name__icontains=search)

    paginator = Paginator(companies, 10) # Show 10 customers per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'companies.html', context)
    




def add_customer(request):
    if request.method == 'POST':
        # Create form and validate data
        form = CustomerForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('customers') 
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})
