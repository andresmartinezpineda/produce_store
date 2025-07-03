from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .forms import CategoryForm,ProductForm
from .models import Category,Product
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Displays the home page.
    """
    return render(request,'home.html')

def signup(request):
    """
    Handles user registration:
    - Shows signup form on GET request.
    - Creates user account on valid POST request.
    """
    if request.method == 'GET':
        # Display the signup form
        return render(request,'signup.html',{
            'form': UserCreationForm
        })
    else:
        # Process form submission
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Attempt to create a new user
                user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                user.save()
                return redirect('signin') # Redirect to login after successful signup
            except:
                # Username already exists or another error occurred
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
        else:
            # Passwords do not match
            return render(request,'signup.html',{
                'form': UserCreationForm,
                'error': 'Passwords do not match'
            })

def signin(request):
    """
    Handles user login:
    - Shows login form on GET request.
    - Authenticates user on POST request.
    """
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form': AuthenticationForm
        })
    else:
        # Authenticate user credentials
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])

        # Invalid credentials
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            # Login successful
            login(request,user)
            return redirect('home')

@login_required
def signout(request):
    """
    Logs the user out and redirects to the login page.
    """
    logout(request)
    return redirect('signin')

@login_required
def category_create(request):
    """
    Handles category creation:
    - Displays the form on GET request
    - Processes form submission on POST request
    """
    if request.method == 'GET':
        # Render empty category form
        return render(request, 'categories/category_create.html', {
            'form': CategoryForm()
        })
    
    else:
        # Process form submission
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            # Save category if form is valid
            new_category = form.save(commit=False)
            new_category.user = request.user

            exists = Category.objects.filter(name=new_category,user=request.user).exists()

            if exists:
                return render(request,'categories/category_create.html',{
                    'form': form,
                    'error': 'You already have a category with that name.'
                })

            new_category.save()
            return redirect('home')
        else:
            # Form has errors, re-render with existing data and error message
            return render(request, 'categories/category_create.html', {
                'form': form,
                'error': 'Please correct the errors below.'
            })

@login_required
def product_create(request):
    """
    Handles the creation of a new product:
    - Displays form on GET request
    - Processes form submission on POST request
    """
    if request.method == 'GET':
        return render(request,'products/product_create.html',{
            'form': ProductForm(user=request.user)
        })
    else:
        form = ProductForm(request.POST,user=request.user)

        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('all_products')
        else:
            return render(request,'products/product_create.html',{
                'form': form,
                'error': 'Please correct the errors below.'
            })

@login_required
def edit_product(request,product_id):
    """
    Allows logged-in users to edit their own products.
    """
    product = get_object_or_404(Product,pk = product_id,user=request.user)
    if request.method == 'GET':
        return render(request,'products/edit_product.html',{
            'form': ProductForm(instance=product),
            'product': product
        })
    else:
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            product_updated = form.save(commit=False)
            product_updated.user = request.user
            product_updated.save()
            return redirect('all_products')
        else:
            return render(request,'products/edit_product.html',{
                'form': form,
                'product': product,
                'error': 'Please correct the errors below.'
            })

@login_required
def delete_product(request,product_id):
    """
    Deletes a product belonging to the authenticated user.
    Only accepts POST requests for safety.
    """
    product = get_object_or_404(Product,pk=product_id,user=request.user)

    if request.method == 'POST':
        product.delete()
        return redirect('categories')
    
    else:
        return redirect('categories')

@login_required
def all_products(request):
    """
    Displays all products for the authenticated user.
    """
    products = Product.objects.filter(user=request.user).order_by('category','name')
    return render(request,'products/all_products.html',{
        'products': products
    })

@login_required
def categories_manage(request):
    """
    Displays all categories for the authenticated user with management options (edit, delete).
    """
    return render(request,'categories/categories_manage.html',{
        'categories': Category.objects.filter(user=request.user).order_by('name')
    })

@login_required
def edit_category(request,category_id):
    """
    Edit an existing category owned by the authenticated user.
    """
    category = get_object_or_404(Category,pk= category_id,user=request.user)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request,'categories/edit_category.html',{
            'form': form,
            'category': category
        })

    else:    
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            updated_category = form.save(commit=False)
            updated_category.user = request.user
            updated_category.save()
            return redirect('categories_manage')
        
        else:
            return render(request, 'categories/edit_category.html', {
                'form': form,
                'category': category,
                'error': 'Please correct the errors below.'
            })

@login_required
def delete_category(request,category_id):
    """
    Allows authenticated users to delete their own categories via POST request
    from the edit_category template.
    """
    if request.method == 'POST':
        category = get_object_or_404(Category,pk=category_id,user=request.user)
        category.delete()
    
    return redirect('categories_manage')






