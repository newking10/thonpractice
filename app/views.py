from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from  .forms import CustomerRegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.views import View

# Create your views here.
def city(request):
    return render(request,'app/demo.html')

#def student(request) :
#    if request.method=='POST':
#        fm= CustomerRegistrationForm(request.POST)
#        if fm.is_valid():
#            fm.save()
#            messages.success(request,'your account has been created successfully')
#            
#    else:
#        fm= CustomerRegistrationForm()        
#    return render(request,'app/studentform.html',{'form':fm}) 
#class CustomerRegistrationView(View):
#    def get(self,request):
#        form=CustomerRegistrationForm()
#        return render(request,'app/studentform.html',{'form':form})
#    def get(self,request):
#        form=CustomerRegistrationForm(request.POST)
#        if form.is_valid():
#            messages.success(request,'congratulations form submitted successfullt')
#            form.save()
#        return render(request,'app/studentform.html',{'form':form})  
                                                         
def signupform(request):
    if request.method=='POST':
        form=CustomerRegistrationForm(request.post)
        if form.is_valid():
            messages.success(request,'congratulations form submitted successfullt')
            form.save()
    else:
        form=CustomerRegistrationForm()        
        
    return render(request,'app/studentform.html',{'form':form})  

def loginform(request):
    if not request.user.is_authenticated:
        if request.method== "POST":
            am = LoginForm(request=request,data=request.POST)
            if am.is_valid():
                uname = am.cleaned_data['username']
                
                upass =am.cleaned_data['password']
                kser = authenticate(username=uname,password=upass)
                if kser is not None:
                
                    login(request , kser)
                    return HttpResponseRedirect("/profile/")
                else:
                    pass    


                
                
               
        else:
           am=LoginForm()            
    
                   
        
        return render(request,'app/loginform.html',{'form':am}) 
    else:
        return HttpResponseRedirect('/profile/')    


      
     
def profileform(request):
    if request.user.is_authenticated:
        return render(request,'app/profile.html')
    else:
        return  HttpResponseRedirect('/loginform/') 


def logoutform(request):
    logout(request) 
    return HttpResponseRedirect('/loginform/')   
def changepassword(request):
    if request.user.is_authenticated:

        if request.method=='POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user )
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm( user=request.user )

        return render(request,'app/changepassword.html',{'form':fm}) 
    return HttpResponseRedirect('/loginform/')       


          

