from typing import Any, Dict
from django import forms
# from PIL import Image
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import ImageDraw

from mainapp.models import CustomUser



class CreateUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'surname', 'email', 'gender', 'password', 'avatar')

    # def clean_avatar(self):
    #     avatar = self.files['avatar']
    #     image = Image.open("avatar")
    #     print(avatar)
    #     return super().clean()