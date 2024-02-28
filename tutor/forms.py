from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TutorAccount




class TutorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    image = forms.ImageField(label='Profile Picture', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','subject' ,'email','phone_no','location','password1', 'password2','image']
        
    def save(self, commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            phone_no = self.cleaned_data.get('phone_no')
            location = self.cleaned_data.get('location')
            subject = self.cleaned_data.get('subject')
            image = self.cleaned_data.get('image')

            TutorAccount.objects.create(
                user = our_user,
                phone_no = phone_no,
                location = location,
                subject = subject,
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
    



class TutorUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    image = forms.ImageField(label='Profile Picture', required=False)
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                user_account = self.instance.account
            except TutorAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['phone_no'].initial = user_account.phone_no
                self.fields['location'].initial = user_account.location
                self.fields['subject'].initial = user_account.subject
                # self.fields['image'].initial = user_account.image
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit == True:
            user.save()
            user_account, created = TutorAccount.objects.get_or_create(user=user)
            user_account.phone_no = self.cleaned_data['phone_no']
            user_account.location = self.cleaned_data['location']
            user_account.subject = self.cleaned_data['subject']
            user_account.image = self.cleaned_data['image']
            user_account.save()
        return user