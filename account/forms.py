from django import forms
from django.forms import ModelForm
from account.models import Page


class userRejistrationForm(forms.Form): 
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField()
  firstname = forms.CharField()
  lastname = forms.CharField()


class userLoginForm(forms.Form): 
 
  username = forms.CharField()
  password = forms.CharField(widget = forms.PasswordInput(render_value = True))

class pageCreateForm(ModelForm):
    class Meta:
       model =   Page    
       fields = [ 'name' , 'order' , 'pageENnam' , 'url', 'dis' , 'PageCate']

"""
class pageCreateForm(forms.Form) :
   name = forms.CharField()
   order = forms.IntegerField()
   pageENnam = forms.CharField()
   url = forms.CharField()
   dis = forms.CharField()
   PageCate  = forms.CharField()
    
"""


  
    