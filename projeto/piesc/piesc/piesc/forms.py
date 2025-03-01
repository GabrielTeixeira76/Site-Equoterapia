from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

class CadastroForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
