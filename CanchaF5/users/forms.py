from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = ('username','first_name', 'surname', 'dni','email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'surname','dni','email',)