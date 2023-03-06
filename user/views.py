from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user = CustomUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('users:login')
        print(user.errors)
        return redirect('users:register')


@login_required
def profile_view(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(pk=request.user.pk)
        update_user = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if update_user.is_valid():
            update_user.save()
        print(update_user.errors)
    user = CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'profile.html', {'user': user})


@login_required
def delete_profile_image(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    user.image.delete()
    return redirect('users:profile')


def password_reset(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_user = CustomUser.objects.filter(Q(email=data))
            if associated_user.exists():
                for user in associated_user:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('users:password-reset-done')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html",
                  context={"password_reset_form": password_reset_form})
