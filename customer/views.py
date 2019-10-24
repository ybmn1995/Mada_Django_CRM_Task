from django.shortcuts import render, redirect  
from customer.forms import CustomerForm  
from customer.models import Customer  
# Create your views here.  
def cust(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    customers = Customer.objects.all()  
    return render(request,"show.html",{'customers':customers})  
def edit(request, id):  
    customer = Customer.objects.get(id=id)  
    return render(request,'edit.html', {'customer':customer})  
def update(request, id):  
    customer = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'customer': customer})  
def destroy(request, id):  
    customer = Customer.objects.get(id=id)  
    customer.delete()  
    return redirect("/show")  