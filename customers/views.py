from django.shortcuts import render

# Create your views here.




# Create your views here.
#@login_required
def customers_view(request):
    return render(request,'customers.html',{'user':request.user})
