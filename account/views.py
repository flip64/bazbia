from  customer.models import Member, Level
from account.models import Role,Page, AccessList
from account.forms import pageCreateForm
from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from account.forms import userRejistrationForm,userLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from django.views.decorators.csrf import csrf_exempt
from config.baseClass import accesspage,accessToModir 







##################################### کلاسهای اصلی 


 
# ثبت نام کاربر جدید  
def user_register(request): 
   if request.method == 'POST' :
     form = userRejistrationForm(request.POST)
     if form.is_valid():
       cd = form.cleaned_data
       user = User.objects.create_user(username=cd['username'],
                                       email=cd['email'] ,
                                       password = cd['password'] , 
                                       first_name =cd['firstname'] ,
                                       last_name= cd['lastname'] )
       
### تعریف عضو جدید        
       Member.objects.create(
          user = user ,
          level =  Level.objects.get(),
          role = Role.objects.get(englishName = 'customer'),
          etebar = 0 
          )
       messages.success(request , 'user registered successfully' ,'success')
       return HttpResponseRedirect('/')
   if request.method == 'GET' :  
     form = userRejistrationForm()
   return render(request , 'account/user_regester.html' , {'form':form})

#   login user 
@csrf_exempt
def user_login(request):
 if request.method == 'POST' : 
    form = userLoginForm(request.POST)
    if form.is_valid() : 
       cd = form.cleaned_data 
       user = authenticate(request ,username = cd['username'] , password = cd['password'])
       if user is not None: 
          login(request , user) 
          return redirect("/")
       else:
        return HttpResponseRedirect('/')
       
 else:
    form = userLoginForm()
 return render(request , 'account/user_login.html', {'form' : form})    


# logout user 
def user_logout(request):
  
  logout(request)
  return redirect('user_login')


#  ساخت صفخه جدید
def pageCreate(request):
  
  if not accesspage(request):
    return redirect('user_login')
  
  

  if request.method == "POST" : 
    form = pageCreateForm(request.POST)
    if form.is_valid(): 
      cd = form.cleaned_data
      Page.objects.create(
        name= cd['name'],
        pageENnam = cd['pageENnam'],
        order = cd['order'],
        url = cd['url'],
        dis = cd['dis'],
        PageCate = cd['PageCate']
      )
    return HttpResponseRedirect("/account/pagelist/")

  if request.method == 'GET' :
    form = pageCreateForm()
     
  return render(request, "account/pagecreate.html", {"form": form})

 
#  ویرایش صفحه 
def pageUpdate(request): 
   if not accesspage(request):
    return redirect("user_login")


   pageID = request.GET['id']
   page = Page.objects.get(id=pageID)

   if request.method == "POST" : 
     form = pageCreateForm(request.POST,instance=page)
    
     if form.is_valid(): 
      form.save()

      return redirect("pagelist")


   if request.method == 'GET' :
     form = pageCreateForm(instance=page)
     
   return render(request, "account/update_page.html", {"form": form})

 
##  لیست صفحات سیستم 
def pageList(request):  
   if  not accesspage(request) : 
       return redirect("/account/userlogin")


   pagelist = Page.objects.all().order_by('order')
   context = {
     'list' :pagelist
   }
   return render(request,'account/pagelist.html',context) 


#  لیست رولهای سیستم 
def roleList(request):  

   if  not accesspage(request) : 
       return redirect("/account/userlogin")


   roleList = Role.objects.all()
   context = {
     'list' :roleList
   }
   return render(request,'account/rolelist.html',context) 


#  با لا بردن مرتبه صفحه در نمایش  دادن 
def upOrder(request): 
   id = int(request.GET['id'])
   state = (request.GET['state'])
   page = Page.objects.get(id= id)
   if state == 'u' :
    if page.order > 1 :
      page.order = page.order - 1 
   if state == 'd': 
      page.order = page.order + 1   
   
   
   page.save()
   pagelist = Page.objects.all().order_by('order')
   context = {
     'list' :pagelist
   }
   return render(request,'account/pagelist.html',context) 


#  لیست  دسترسی رولها به صفحات سیستم  
def accesslist(request) :
    
    if  not accesspage(request) : 
       return redirect("/account/userlogin")


    id = request.GET['id']
    role = Role.objects.get(id=id)
    accesslist  = AccessList.objects.filter(role =role)
    pageList=[]
    for li in accesslist: 
        pageList.append(li.page)


    list = Page.objects.all()
    listNotAccessPage=[]
    for li in list: 
      listNotAccessPage.append(li)


    for li in pageList: 
        listNotAccessPage.remove(li)


    context = {
      'listAccessPage' : pageList,
      'listNotAccessPage' : listNotAccessPage,
      'role' : role
    }
    return render(request,'account/acceelist.html',context) 
 




#  اضافه کردن دسترسی صفحات به رولهای سیستم   
def addAcessview(request):


  if  not accesspage(request) : 
       return redirect("/account/userlogin")

  
  role =  Role.objects.get(id = int(request.GET['roleid']))
  page =  Page.objects.get(id = int(request.GET['pageid']))
  try:
    AccessList.objects.get(role=role , page = page) 
  except:
    AccessList.objects.create(role=role, page =page)

  context = {
   }
  return HttpResponseRedirect("/account/accessList/?id="+str(role.id))

  

#  حذف کردن دسترسی صفحات به رولهای سیستم   
def removeAccessView(request):
  if  not accesspage(request) : 
       return redirect("/account/userlogin")



  role =  Role.objects.get(id = int(request.GET['roleid']))
  page =  Page.objects.get(id = int(request.GET['pageid']))
  
  access = AccessList.objects.get(role=role , page = page) 
  access.delete()
  return HttpResponseRedirect("/account/accessList/?id="+str(role.id))






















