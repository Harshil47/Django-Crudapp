# views.py
from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import Supplier, Customer, Place, Driver, Lorry, Product, UserInput

def add_data(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            try:
                # Extract data from the form
                supplier_name = form.cleaned_data['supplier']
                customer_name = form.cleaned_data['customer']
                place_name = form.cleaned_data['place']
                driver_name = form.cleaned_data['driver']
                lorry_no = form.cleaned_data['lorry']
                purchase_challan = form.cleaned_data['purchase_challan']
                sales_challan = form.cleaned_data['sales_challan']
                product_name = form.cleaned_data['product']
                driver_name_field = form.cleaned_data['driver_name']
                no_of_trip = form.cleaned_data['no_of_trips']
                date1 = form.cleaned_data['date_input1']
                date2 = form.cleaned_data['date_input2']
                date3 = form.cleaned_data['date_input3']

                # Update or create new values in the datasets
                try:
                    supplier_obj = Supplier.objects.get(name=supplier_name)
                except Supplier.DoesNotExist:
                    supplier_obj = Supplier.objects.create(name=supplier_name)

                try:
                    customer_obj = Customer.objects.get(name=customer_name)
                except Customer.DoesNotExist:
                    customer_obj = Customer.objects.create(name=customer_name)

                try:
                    place_obj = Place.objects.get(name=place_name)
                except Place.DoesNotExist:
                    place_obj = Place.objects.create(name=place_name)

                try:
                    driver_obj = Driver.objects.get(name=driver_name)
                except Driver.DoesNotExist:
                    driver_obj = Driver.objects.create(name=driver_name)

                try:
                    lorry_obj = Lorry.objects.get(lorry_no=lorry_no)
                except Lorry.DoesNotExist:
                    lorry_obj = Lorry.objects.create(lorry_no=lorry_no)

                try:
                    product_obj = Product.objects.get(name=product_name)
                except Product.DoesNotExist:
                    product_obj = Product.objects.create(name=product_name)

                # Create a new UserInput object and save it to the database
                UserInput.objects.create(
                    supplier=supplier_obj,
                    customer=customer_obj,
                    place=place_obj,
                    driver=driver_obj,
                    lorry=lorry_obj,
                    purchase_challan_no=purchase_challan,
                    sales_challan_no=sales_challan,
                    product=product_obj,
                    driver_name=driver_name_field,
                    no_of_trips=no_of_trip,
                    date_input1=date1,
                    date_input2=date2,
                    date_input3=date3
                )
                form.save()
                return redirect('success')
            except Exception as e:
                print("Exception during form processing:", e)

    else:
        form = UserInputForm()

    suppliers = Supplier.objects.all()
    customers = Customer.objects.all()
    places = Place.objects.all()
    drivers = Driver.objects.all()
    lorries = Lorry.objects.all()
    products = Product.objects.all()

    return render(request, 'add_data.html', {
        'form': form,
        'suppliers': suppliers,
        'customers': customers,
        'places': places,
        'drivers': drivers,
        'lorries': lorries,
        'products': products,
    })

def success(request):
    user_inputs = UserInput.objects.all()
    return render(request, 'success.html', {'user_inputs': user_inputs})
