from django.shortcuts import render


def mod(request):
    return render(request, 'work/base.html')


#****************************************************************
# def home(request):
#     orders = Order.object.all()
#     customers = Customers.object.all()
#     total_customers = customers.count()
#
#     total_orders = orders.count
#     delivered = orders.filter(status='Delivered').count()
#     pending = orders.filter(status='Pending').count()
#
#     context = {'orders': orders, 'customers': customers,
#     'total_orders': total_orders, 'delivered': delivered,
#     'pending': pending}
#     return render(request, 'dashboard/products.html', context)
#
#
# def products(request):
#     products = Product.object.all()
#     return render(request, 'accaunts/products.html', {'products': products})
#
# def customer(request):
#     customer = Customer.object.get(id=pk_test)
#     order_count = orders.count()
#     context = {'customer': customer, 'orders': orders, 'order_count': order_count}
#     return render(request, 'accaunts/customers.html', context)
#***********************************************
# СОЗДАНИЕ ФОРМИ
# def createOrder(request):
#     form = OrderForm()
#     if request.method =='POST':
#         #print('Printing POST:', request.POST)
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         
#     context = {'form': form}
#     return render (request, 'accaunts/order_form.html', context)