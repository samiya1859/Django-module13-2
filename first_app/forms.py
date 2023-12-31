from django import forms
from django.core import validators

# widgets == field to html input



class contactform(forms.Form):
    name = forms.CharField(label="username", initial="Name",help_text="Total length must be within 70 characters",required=False,widget=forms.Textarea(attrs={'id':'textarea','class':'class_1 class_2','placeholder':'Enter your name'}))

    file =  forms.FileField()
    email = forms.EmailField(label="useremail")
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    ChOICES =[('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=ChOICES,widget=forms.RadioSelect)
    meal = [('P','Pepperoni'),('M','Mashrooms'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valuename = self.cleaned_data['name']
    #     if len(valuename) < 10:
    #         raise forms.validation_error("Enter a  name with at least 10 characters")
    #     return valuename
    # def clean_mail(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must conrtain .com")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname)>10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
        
    #     if '.com not in valemail':
    #         raise forms.ValidationError("Your email must contain .com")
        
def length_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter a value at least 10 characters")    

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10,message="Enter a name with at most 10 characters")])
    text = forms.CharField(widget=forms.TextInput,validators=[length_check])
    email = forms.CharField(validators=[validators.EmailValidator(message="Enter a vaild email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(40,message="Age must be max 40"),validators.MinValueValidator(20,message="age must be at least 20")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="file extension must be begin with pdf")])


class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name)<15:
            raise forms.ValidationError("Name must be at least 15 characters")