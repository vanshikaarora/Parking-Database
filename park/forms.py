from django import forms

from .models import Post, DatePost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('vehicleType', 'number', 'amount', 'timeIn', 'timeOut','date')


class DateForm(forms.ModelForm):

    class Meta:
        model=DatePost
        fields = ('vehicleNumber','date')