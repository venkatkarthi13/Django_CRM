from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Records

class SignupForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    first_name=forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    last_name=forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
        
    def __init__(self,*args,**kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class= "form-text text-muted"><small>Required. 150 characters or fewer letters, digits and @/./+/-/_only.</small></span>'
        
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class= "form-text text-muted" small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain atleast 8 characters.</li><li>Your password can\'t be too commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='confirm password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<span class= "form-text text-muted"><small>Enter the same password as before, for verification.</small> '
        

class addRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First name","class":"form-control"}),label="")
    last_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"last name","class":"form-control"}),label="")
    email =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}),label="")
    phone=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone","class":"form-control"}),label="") 
    address=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}),label="")
    city=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}),label="")
    state=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State","class":"form-control"}),label="")
    zipcode=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode","class":"form-control"}),label="")
    
    class Meta:
        model=Records
        exclude=("user",)