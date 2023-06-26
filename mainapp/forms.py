from django import forms

from mainapp.models import CustomUser



class CreateUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'surname', 'email', 'gender', 'password', 'avatar')
