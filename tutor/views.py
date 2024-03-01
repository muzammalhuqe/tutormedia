from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from django.views import View
from django.core.mail import EmailMultiAlternatives
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import TutorRegistrationForm, TutorUpdateForm
from .models import TutorAccount
from django.views.generic import DetailView



class TutorRegistrationView(CreateView):
    form_class = TutorRegistrationForm
    template_name = 'tutor_singup.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        user = form.save(commit=False)
        user.is_active = False
        
        # Access cleaned_data from the form instance
        phone_no = form.cleaned_data.get('phone_no')
        location = form.cleaned_data.get('location')
        subject = form.cleaned_data.get('subject')
        image = form.cleaned_data.get('image')

        TutorAccount.objects.create(
            user=user,
            phone_no=phone_no,
            location=location,
            subject=subject,
            image=image,
        )
        user.save()
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link = f"https://tutormediabd.onrender.com/accounts/active/{uid}/{token}"
        email_subject = "Confirm Your Email"
        email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
        
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        return redirect('homepage')


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('signup')



# class TutorLoginView(LoginView):
#     template_name = 'tutor_login.html'

#     def get_success_url(self):
#         return reverse_lazy('profile')
    
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(reverse_lazy('profile'))
#         return super().dispatch(request, *args, **kwargs)



# @login_required
# def Tutorprofile(request):
#     tutor = request.user
#     tutorprofile = TutorAccount.objects.get(user=tutor)

#     if request.method == 'POST':
#         tutor_form = TutorUpdateForm(request.POST, request.FILES, instance=tutor)
#         if tutor_form.is_valid():
#             tutor_form.save()
#             return redirect('tutorprofile')
#     else:
#         tutor_form = TutorUpdateForm(instance=tutor)

#     return render(request, 'tutorprofile.html', {'tutor_form': tutor_form, 'tutorprofile': tutorprofile})






class TutorDetailView(DetailView):
    model = TutorAccount
    template_name = 'tutor_detail.html'
    context_object_name = 'tutor'
    pk_url_kwarg = 'id'
