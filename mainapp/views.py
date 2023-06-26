from django.contrib.auth import get_user_model

from django.views.generic import TemplateView, CreateView

from mainapp.forms import CreateUserForm



class RegisterView(CreateView):
    template_name = 'register.html'
    model = get_user_model()
    form_class = CreateUserForm
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return super().get_context_data(**kwargs)
