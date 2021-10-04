from django.contrib.auth.forms import (UserCreationForm,
                                     UserChangeForm,
                                     AuthenticationForm
                                    )

from .models import (CustomUser, Game, Category)
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets                                       



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','username','first_name','last_name',) 


class CreatGameForm(ModelForm):
    

    class Meta:
        model = Game
        fields = ['title','category','image','start_date','end_date']
    
    category = forms.ModelMultipleChoiceField(
        queryset = Category.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    