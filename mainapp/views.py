import os
from django.contrib.auth import get_user_model
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from mainapp.forms import CreateUserForm
from config import settings
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class RegisterView(CreateView):
    template_name = 'register.html'
    model = get_user_model()
    form_class = CreateUserForm
    success_url = 'user.html'

    def watermark_photo(self, avatar):
        image_path = os.path.join(os.getcwd(), settings.MEDIA_ROOT, 'avatars', avatar)
        # base_image = Image.open(image_path)
        # watermark_path = os.path.join(os.getcwd(), settings.MEDIA_ROOT, settings.WATERMARK)
        photo = Image.open(image_path)
        draw = ImageDraw.Draw(photo)
        font = ImageFont.load_default()
        width, height = photo.size
        margin = 300
        textwidth, textheight = draw.textsize(settings.WATERMARK, font)
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x,y), settings.WATERMARK, (255, 255, 255), font=font)
        photo.save(image_path)



    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        print(f"type {type(form.files['avatar'])}, {form.files['avatar'].name}")
        self.watermark_photo(form.files['avatar'].name)
        return super(RegisterView, self).form_valid(form)
    

class UserDetailView(DetailView):
    template_name = 'user.html'
    model = get_user_model()
    # form_class = CreateUserForm
