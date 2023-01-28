from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CreateUserForm
from accounts.models import Vendee, OrderItems


class VendeeSignUpView(CreateView):
    """
    Creates new employee
    """
    template_name = 'account/registration.html'
    form_class = CreateUserForm

    def get(self, request, *args, **kwargs):
        # Use RequestContext instead of render_to_response from 3.0
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_vendee = True
            # user.set_password(form.cleaned_data['password'])
            user.save()
            Vendee.objects.create(user=user)

            # user = U.objects.get(email=user.email)
            return redirect('login')
        return render(request, self.template_name, {'form': form})


