from django.shortcuts import render
from customers.models import Customer , Company
from customers.models   import CustomerForm
# Create your views here.





# Create your views here.
#@login_required
def customers_view(request):
    return render(request,'customers.html',{'user':request.user})


def customer_list(request):
    customers = Customer.objects.all()
    companies = Company.objects.all()
    context = {
        'customers': customers,
        'companies': companies
    }
    return render(request, 'customers.html', context)

def add_customer(request):
    if request.method == 'POST':
        # Create form and validate data
        form = CustomerForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('customer_list') 
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})
