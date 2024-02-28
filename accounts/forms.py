from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccount

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    ssc_roll = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    ssc_gpa = forms.DecimalField(widget=forms.TextInput(attrs={'id' : 'required'}))
    image = forms.ImageField(label='Profile Picture', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','ssc_roll','ssc_gpa','password1', 'password2','image']
        
    def save(self, commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            ssc_roll = self.cleaned_data.get('ssc_roll')
            ssc_gpa = self.cleaned_data.get('ssc_gpa')
            image = self.cleaned_data.get('image')

            UserAccount.objects.create(
                user = our_user,
                ssc_roll = ssc_roll,
                ssc_gpa = ssc_gpa,
                image=image,
            )
            return our_user
        
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError({'error' : "Email Already exists"})
        
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        account.set_password(password)
        account.save()
        return account
    

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    ssc_roll = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    ssc_gpa = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    image = forms.ImageField(label='Profile Picture', required=False)
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email','ssc_roll','ssc_gpa']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['ssc_roll'].initial = user_account.ssc_roll
                self.fields['ssc_gpa'].initial = user_account.ssc_gpa
                # self.fields['image'].initial = user_account.image
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit == True:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_account.ssc_roll = self.cleaned_data['ssc_roll']
            user_account.ssc_gpa = self.cleaned_data['ssc_gpa']
            user_account.image = self.cleaned_data['image']
            user_account.save()
        return user


