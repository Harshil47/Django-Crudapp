from django.shortcuts import redirect, render , get_object_or_404
from .forms import OrderForm,  CustomerForm, BillingForm
from .models import Orders, Customer, Product, Billing
from django.db.models import Q
import csv
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from .forms import calculate_amount
from datetime import datetime
from django.db.models import Sum, F
from django.utils.datetime_safe import datetime
from django.views.decorators.http import require_POST
from django.db.models import  Min ,Max
import itertools
from django.db import transaction
# Create your views here.
def orderFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_instance = form.save(commit=False)
            
            # Call the calculate_amount function and set the amount field
            order_instance.amount = calculate_amount(order_instance)
            
            # Save the order instance with the calculated amount
            order_instance.save()
            
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)
'''
def showView(request):
    query = request.GET.get('q', '')
    
    if query:
        obj = Orders.objects.filter(Q(fname__icontains=query))
    else:
        obj = Orders.objects.all()

    template_name = 'crudapp/show.html'
    context = {'obj': obj, 'query': query}
    return render(request, template_name, context)
'''
def showView(request):
    supplier_query = request.GET.get('q', '')
    customer_query = request.GET.get('customer', '')
    sales_challan_date_query = request.GET.get('sales_challan_date', '')

    obj = Orders.objects.all()

    if supplier_query:
        obj = obj.filter(Q(fname__icontains=supplier_query))
    if customer_query:
        obj = obj.filter(Q(Cname__icontains=customer_query))
    if sales_challan_date_query:
        sales_challan_date = datetime.strptime(sales_challan_date_query, '%Y-%m-%d').date()
        obj = obj.filter(df3=sales_challan_date)

    template_name = 'crudapp/show.html'
    context = {'obj': obj, 'query': supplier_query}
    return render(request, template_name, context)


def updateView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Order ID', 'Supplier Name', 'Place', 'Driver Name', 'Lorry number', 'Purchase Challan no.', 'Sales Challan no.', 'Product Name', 'pcs/Fts', 'Number of trips', 'Date Field 1', 'Date Field 2', 'Date Field 3'])

    orders = Orders.objects.all()
    for order in orders:
        writer.writerow([order.oid, order.fname, order.Pname, order.Dname, order.Lno, order.pcno, order.scno, order.Product, order.pcs, order.trip, order.df1, order.df2, order.df3])

    return response


def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_info_url')  # Redirect to the customer info page
    else:
        form = CustomerForm()

    return render(request, 'crudapp/customer_add.html', {'form': form})


def customer_info(request):
    # Get the search query from the URL parameter 'q'
    query = request.GET.get('q', '')

    # If a query is provided, filter customers based on the name
    if query:
        customers = Customer.objects.filter(Q(Cname__icontains=query))
    else:
        # If no query, fetch all customers
        customers = Customer.objects.all()

    # Render the customerInfo.html template with the customers and query
    template_name = 'crudapp/customerInfo.html'
    context = {'customers': customers, 'query': query}
    return render(request, template_name, context)



    
def get_product_details(request, product_id):
    try:
        # Query the Product model to get details based on the product_id
        product = Product.objects.get(name=product_id)

        # Example response data
        data = {
            'name': product.name,
            'rate': product.rate,
            'quantity_per': product.quantity_per,
            # Add other fields as needed
        }

        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    


'''

def billView(request):
    if request.method == 'POST':
        selected_rows = request.POST.getlist('selected_rows')

        # Perform any necessary actions with the selected 'oid' values
        # For example, you might want to update the 'billed' field for the selected orders
        Orders.objects.filter(oid__in=selected_rows).update(billed='Yes')

        return redirect('success_url')    
    
    
    
    # Get distinct customer names for the dropdown
    customer_names = Customer.objects.values_list('Cname', flat=True).distinct()

    # Get selected customer name from the dropdown
    selected_customer = request.GET.get('customer', '')

    # Get date range from user input
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # Parse dates if provided
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        start_date = None

    try:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        end_date = None

    # Assuming 'pname' and 'product' are the fields to match
    # Filter based on customer and date range
    bill_items = Orders.objects.filter(
        Cname=selected_customer,
        df3__range=(start_date, end_date),
        billed='No'
    ).values('oid','Pname', 'product').annotate(
        total_trips=Sum('trip'), total_pcs=Sum('pcs')
    )

    template_name = 'crudapp/Bill.html'
    context = {
        'bill_items': bill_items,
        'customer_names': customer_names,
        'selected_customer': selected_customer,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, template_name, context)
'''


def billView(request):
    if request.method == 'POST':
        merged_oids_str = request.POST.get('merged_oids', '')
        
        if merged_oids_str:
            merged_oids = [int(oid) for oid in merged_oids_str.split(',')]
            
            # Perform the update in the database
            Orders.objects.filter(oid__in=merged_oids).update(billed='Yes')

            return redirect('success_url')  
    
    
    
    # Get distinct customer names for the dropdown
    customer_names = Customer.objects.values_list('Cname', flat=True).distinct()

    # Get selected customer name from the dropdown
    selected_customer = request.GET.get('customer', '')

    # Get date range from user input
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    # Parse dates if provided
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        start_date = None

    try:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except (TypeError, ValueError):
        end_date = None

    # Assuming 'pname' and 'product' are the fields to match
    # Filter based on customer and date range
    '''    
    bill_items = Orders.objects.filter(
        Cname=selected_customer,
        df3__range=(start_date, end_date),
        billed='No'
    ).values('Cname','Pname', 'product').annotate(
        merged_oids=ArrayAgg('oid'),oid=Min('oid'),total_trips=Sum('trip'), total_pcs=Sum('pcs')
    )
    '''
   # Assuming 'pname' and 'product' are the fields to match
    # Filter based on customer and date range
    orders = Orders.objects.filter(
        Cname=selected_customer,
        df3__range=(start_date, end_date),
        billed='No'
    ).values('Cname', 'Pname', 'product', 'oid', 'trip', 'pcs', 'AggregatedAmount').order_by('Cname', 'Pname', 'product')

    bill_items = []
    for key, group in itertools.groupby(orders, key=lambda x: (x['Cname'], x['Pname'], x['product'])):
        # Convert the group to a list to check if it's empty
        group_list = list(group)
        if group_list:
            merged_oids = list(item['oid'] for item in group_list)
            oid = min(item['oid'] for item in group_list)
            total_trips = sum(item['trip'] for item in group_list)
            total_pcs = sum(item['pcs'] for item in group_list)
            total_amount = max(item['AggregatedAmount'] or 0 for item in group_list)
            bill_items.append({
                'Cname': key[0],
                'Pname': key[1],
                'product': key[2],
                'merged_oids': merged_oids,
                'oid': oid,
                'total_trips': total_trips,
                'total_pcs': total_pcs,
                'total_amount': total_amount,
            })
            
    with transaction.atomic():
        for bill_item in bill_items:
            total_pcs = bill_item['total_pcs'] or 0
            Orders.objects.filter(oid=bill_item['oid']).update(AggregatedQuantity=total_pcs, mergedOids=','.join(map(str, bill_item['merged_oids'])))

    '''
    # If no filters are applied, include items with billed='No'
    if not selected_customer and not start_date and not end_date:
        bill_items = Orders.objects.filter(billed='No').values('Cname','Pname', 'product').annotate(
            merged_oids=ArrayAgg('oid'),oid=Min('oid'),total_trips=Sum('trip'), total_pcs=Sum('pcs')
        )
    '''
    
    
    if not selected_customer and not start_date and not end_date:
           # Assuming 'pname' and 'product' are the fields to match
    # Filter based on customer and date range
        orders = Orders.objects.filter(
        billed='No'
    ).values('Cname', 'Pname', 'product', 'oid', 'trip', 'pcs', 'AggregatedAmount').order_by('Cname', 'Pname', 'product')

        bill_items = []
        for key, group in itertools.groupby(orders, key=lambda x: (x['Cname'], x['Pname'], x['product'])):
        # Convert the group to a list to check if it's empty
            group_list = list(group)
            if group_list:
                merged_oids = list(item['oid'] for item in group_list)
                oid = min(item['oid'] for item in group_list)
                total_trips = sum(item['trip'] for item in group_list)
                total_pcs = sum(item['pcs'] for item in group_list)
                total_amount = max(item['AggregatedAmount'] or 0 for item in group_list)
                bill_items.append({
                'Cname': key[0],
                'Pname': key[1],
                'product': key[2],
                'merged_oids': merged_oids,
                'oid': oid,
                'total_trips': total_trips,
                'total_pcs': total_pcs,
                'total_amount': total_amount,
                })
        with transaction.atomic():
            for bill_item in bill_items:
                total_pcs = bill_item['total_pcs'] or 0
                Orders.objects.filter(oid=bill_item['oid']).update(AggregatedQuantity=total_pcs, mergedOids=','.join(map(str, bill_item['merged_oids'])))

                
    template_name = 'crudapp/Bill.html'
    context = {
        'bill_items': bill_items,
        'customer_names': customer_names,
        'selected_customer': selected_customer,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, template_name, context)




def rateView(request, oid):
    
    
    order_instance = get_object_or_404(Orders, oid=oid)

    # Fetch the previous bill data
    previous_bill= "None"
    if request.method == 'POST':
        form = BillingForm(request.POST, order_instance=order_instance)
        print("POST data:", request.POST)
        
       
        
        if form.is_valid():
            # Fetch additional fields from the cleaned_data
            oid = request.POST.get('oid')
            product = request.POST.get('product')
            place = request.POST.get('place')

            # Perform calculations
            total_rate = form.cleaned_data['total_rate']
            material_rate = form.cleaned_data['material_rate']
            transport_rate = total_rate - material_rate
            amount = order_instance.AggregatedQuantity * total_rate
            print("transport_rate :",transport_rate)
            print("Amount :",amount)
            order_instance.AggregatedAmount = amount  # Update with your calculation
            order_instance.save()

            # If 'calculate' is in the POST data, return JSON response
            if 'calculate' in request.POST:
                return JsonResponse({
                    'transport_rate': transport_rate,
                    'amount': amount,
                })

            # If 'submit' is in the POST data, save to the Billing model
            elif 'action' in request.POST and request.POST['action'] == 'submit':
                billing_instance = Billing(
                    Cname=order_instance.Cname,
                    bill_date=form.cleaned_data['bill_date'],
                    final_rate=form.cleaned_data['total_rate'],
                    material_rate=form.cleaned_data['material_rate'],
                    transport_rate=transport_rate,
                    final_amount=amount,
                    mcode=form.cleaned_data['mcode'],
                    tcode=form.cleaned_data['tcode'],
                    oid=oid,
                    product=product,
                    place=place
                )

                print("Billing Data:", billing_instance.product)
                billing_instance.save()
                print("Billing Data:", billing_instance.oid)
                # Redirect to a success page or any other page as needed
                return redirect('bill_url')
        else:
            print("Form errors:", form.errors)
    else:
        form = BillingForm(order_instance=order_instance)
        
        previous_bill_condition = {'Cname': order_instance.Cname, 'place': order_instance.Pname}

        previous_bill = Billing.objects.filter(**previous_bill_condition).exclude(oid=oid).order_by('-bill_date')

       # print("Previous Bill Query Condition:")
       # print(previous_bill_condition)
       # print(Billing.objects.filter(**previous_bill_condition).exclude(oid=oid).order_by('-bill_date').query)
        print(previous_bill)
    # Render the form for both GET and POST requests
    return render(request, 'crudapp/rate.html', {'order_instance': order_instance,'form': form, 'previous_bill': previous_bill})
