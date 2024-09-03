from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, CreateView, TemplateView,ListView,UpdateView,DeleteView,DetailView,FormView
from scrap.models import Scraps, Category,UserProfile,Wishlist
from django.contrib import messages
from scrap.forms import UserForm, LoginForm, ProductAddForm, CategoryForm,UserForm,UserProfileForm,PayForm
from django.contrib.auth import authenticate, login, logout
from scrap.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


decs=[login_required,never_cache]

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})
        

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")

            user_object = authenticate(request, username=uname, password=pwd)
            if user_object:
                login(request, user_object)
                print("valid")
                return redirect("home")
            print("invalid")
            return render(request, "login.html", {"form": form})
        


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")
    

@method_decorator(decs,name="dispatch")  
class ProductAddView(View):    
    def get(self,request,*args,**kwargs):
        form=ProductAddForm
        return render(request,"product_add.html",{"form":form})    
    def post(self,request,*args,**kwargs):
        form=ProductAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("home")
        else:
            return render(request,"product_add.html",{"form":form})

@method_decorator(decs,name="dispatch") 
class IndexView(ListView):
    template_name="home.html"
    form_class=ProductAddForm
    model=Scraps
    context_object_name="data"

@method_decorator(decs,name="dispatch")  
class CategoryAddView(CreateView):
    template_name = "category.html"
    form_class = CategoryForm
    model = Category

    def get_success_url(self):
        return reverse("home")

@method_decorator(decs,name="dispatch")      
class ProductListView(ListView):
    template_name="home.html"    
    model=Scraps
    context_object_name="data"



@method_decorator(decs,name="dispatch")  
class ProductUpdateView(UpdateView):
    template_name="product_edit.html"  
    form_class=ProductAddForm
    model=Scraps  

    def get_success_url(self):
        return reverse("home")
    
@method_decorator(decs,name="dispatch")  
class ProductDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Scraps.objects.get(id=id).delete()
        return redirect("home")

@method_decorator(decs,name="dispatch")     
class ProductDetailView(DetailView):
    template_name="product_detail.html"
    model=Scraps
    context_object_name="data"

@method_decorator(decs,name="dispatch")  
class ProfileUpdateView(UpdateView):
    template_name="profile_edit.html"
    form_class=UserProfileForm
    model=UserProfile

    def get_success_url(self):
        return reverse("home")

@method_decorator(decs,name="dispatch")     
class ProfileDetailView(DetailView):
    template_name="profile.html"
    model=UserProfile
    context_object_name="data"


# @method_decorator(decs,name="dispatch")  
# class WishlistView(View):
#     def product_details(request, product_id):
#         product_id=product_id
#         form = WishlistForm(request.POST or None)

#         if request.method == 'POST' and form.is_valid():
#         # Add the product to the user's wishlist
#             if request.user.is_authenticated:
#                request.user.profile.wishlist.add(product_id)

#                return render(request, 'wishlist.html', {'product': product_id, 'form': form})



@method_decorator(decs,name="dispatch")  
class BuyView(DetailView):
    template_name="buy.html"
    model=Scraps
    context_object_name="data" 

@method_decorator(decs,name="dispatch")  
class PayView(View):    
    def get(self,request,*args,**kwargs):
        form=PayForm
        return render(request,"product_add.html",{"form":form})    
    def post(self,request,*args,**kwargs):
        form=PayForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("paym")
        else:
            return render(request,"pay.html",{"form":form})
        

class WishlistAddView(View):
    def post(self,request,args,*kwargs):
        id=kwargs.get("pk")
        scrap_obj=Scraps.objects.get(id=id)
        action=request.POST.get("action")
        print(action)
        wishlist, created =Wishlist.objects.get_or_create(user=request.user)
        if action == "add":
            wishlist.scrap.add(scrap_obj)
        elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
            print("removed")
        return redirect("index")
    
# @method_decorator(decs,name="dispatch")         
# class WishlistView(View):
#     def get(self,request,args,*kwargs):
#         qs=Wishlist.objects.get(user_id=request.user.id)
#         wishitems=Scraps.objects.exclude(user=request.user)
#         return render(request,"wishlist.html",{"data":qs,"items":wishitems})
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         scrap_obj=Scraps.objects.get(id=id)
#         action=request.POST.get("action")
#         wishlist,created=Wishlist.objects.get_or_create(user=request.user)
#         if action =="add":
#           wishlist.scrap.add(scrap_obj)
#         elif action == "remove":
#           wishlist.scrap.remove(scrap_obj)
#         return redirect("home")
           
class WishlistAddView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        scrap_obj=Scraps.objects.get(id=id)
        print(scrap_obj)
        action=request.POST.get("action")
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        if action == "add":
            wishlist.scrap.add(scrap_obj)
            messages.success(request,"Product added to wishlist")
        elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
            print("removed")
            messages.success(request,"Product Removed from wishlist")
        elif action == "remove_from_wish":
            wishlist.scrap.remove(scrap_obj)
            return redirect("wishlistview")
        return redirect("home")
    
@method_decorator(decs,name="dispatch")
class WishlistView(View):
    def get(self,request,*args,**kwargs):
        qs=Wishlist.objects.get(user_id=request.user.id)
        wishitems=Scraps.objects.exclude(user=request.user)
        return render(request,"wishlist.html",{"data":qs,"items":wishitems})
    

class PaymentView(FormView):
    form_class=PayForm
    template_name="pay.html"
    
    def get_success_url(self):
        return reverse("paym")
    


class PaymentdetailView(TemplateView):
    template_name="payment.html"    