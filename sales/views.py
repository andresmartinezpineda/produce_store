from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop_admin.models import Product
from .models import Sale, SaleItem
from .forms import ProductSearchForm
from decimal import Decimal
from django.utils import timezone
from django.http import JsonResponse

@login_required
def create_sale(request):
    """
    Allows logged-in users to register a sale by adding multiple products with quantity and price.
    Includes a product search system.
    """
    products = [] # Empty list to store the products found during the search

    if 'search' in request.GET:
    # Checks if the URL contains a parameter called "search"

        search_query = request.GET.get('search')
        # Gets the value of the "search" parameter and stores it in the variable search_query

        products = Product.objects.filter(user=request.user, name__icontains=search_query)
        # Filters the products that:
        # - Belong to the logged-in user (request.user)
        # - Contain the search string in their name, case-insensitive (icontains)

    if request.method == 'POST':
    # Checks if the request is of type POST (form submission)

        product_ids = request.POST.getlist('product_id')
        # Retrieves a list of product IDs sent from hidden inputs in each row of the table

        quantities = request.POST.getlist('quantity') 
        # Retrieves a list of quantities for each product, sent from the quantity inputs in the table

        prices = request.POST.getlist('price')
        # Retrieves a list of prices for each product, sent from the price inputs in the table

        if not product_ids: 
        # If the product_ids list is empty, it means there are no products in the table

            messages.error(request, "You must add at least one product.") 
            # Sends an error message to be displayed in the template (i haven't configured the display yet)

            return redirect('create_sale')
            # Redirects back to the "create_sale" page

        sale = Sale.objects.create(user=request.user, date=timezone.now(), total=0)
        # Creates a record in the Sale table with the current user, current date, and initial total set to 0
        # The record is saved to the database immediately

        total = Decimal('0.00')
        # Initializes the total variable as a Decimal to accumulate the sale total and avoid precision errors with money

        for i in range(len(product_ids)):
        # Loop that iterates over each index of the product_ids list

            try:
                product = Product.objects.get(pk=product_ids[i], user=request.user)
                # Searches for the product in the database that matches the ID at position 'i' of 'product_ids' 
                # and belongs to the current user

                quantity = Decimal(quantities[i])
                # Converts the value at position 'i' of 'quantities' to Decimal and stores it in 'quantity'

                price = Decimal(prices[i])
                # Converts the value at position 'i' of 'prices' to Decimal and stores it in 'price'

                SaleItem.objects.create(
                    sale=sale, # Associates the "sale" detail with the previously created "sale"
                    product=product, # Product obtained in the current iteration
                    quantity=quantity, # Quantity of the product
                    price=price  # Unit price of the product
                )
                total += quantity * price 
                # Adds to the total the value corresponding to quantity multiplied by price of the current product

            except:
                continue  # Ignore invalid or manipulated data

        sale.total = total
        # Updates the 'total' field of the 'sale' object with the accumulated value

        sale.save()
        # Saves the 'sale' object to the database, now with the updated total

        messages.success(request, "Sale registered successfully.")
        # Sends a success message to the user after registering the sale

        return redirect('create_sale')
        # Redirects back to the create_sale view

    search_form = ProductSearchForm(request.GET or None)
    # Creates an instance of the search form
    # If there are parameters in the URL (GET method), uses them to initialize the form; otherwise, leaves it empty

    context = {
    # Creates a dictionary

        'search_form': search_form,# Key that contains the search form to be sent to the template
        'products': products, # Key that contains the list of filtered products or an empty list
    }
    return render(request, 'sales/create_sale.html', context)
    # Renders the 'create_sale.html' template and sends it the 'context' dictionary to display the form and products


@login_required
def product_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(user=request.user, name__icontains=query)
    results = [{'id': p.id, 'name': p.name, 'price': float(p.price)} for p in products]
    return JsonResponse(results, safe=False)
