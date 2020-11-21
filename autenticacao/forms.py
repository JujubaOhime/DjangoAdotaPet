import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ChoiceField, DateInput, RadioSelect, Select

from autenticacao.models import Profile


class AuthenticationFormCustomizado(AuthenticationForm):

    error_messages = {
        'invalid_login': 'Login inválido'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].error_messages={'required': 'Campo obrigatório'}
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário'})

        self.fields['password'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha'})


class UsuarioFormCustomizado(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = 'Nome'
        self.fields['first_name'].required = True
        self.fields['password2'].minlength = 3

        self.fields['last_name'].label = 'Sobrenome'
        self.fields['last_name'].required = True
        self.fields['password2'].minlength = 3

        self.fields['email'].label = 'Email'
        self.fields['email'].required = True
        self.fields['email'].error_messages = {'invalid': 'O campo Email é inválido.'}

        self.fields['username'].label = 'Usuário'
        self.fields['username'].error_messages = {
            'invalid': 'Usuário inválido. Use letras, números, @, ., +, -, _',
            'unique': 'Usuário já cadastrado.'
        }
        self.fields['username'].minlength = 3

        self.fields['password1'].label = 'Senha'
        self.fields['password1'].maxlength = 128

        self.fields['password2'].label = 'Confirmação de Senha'
        self.fields['password2'].maxlength = 128

        for field in self.fields.values():
            field.error_messages['required'] = \
                'Campo {nome_do_campo} de preenchimento obrigatório'.format(nome_do_campo=field.label)

        self.fields['password1'].validators.append(self.validate_password_strength)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',
                  'password1', 'password2')
        widgets = {

        }
    error_messages = {
        'password_mismatch': 'As senhas informadas não conferem.'
    }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        usuarios = User.objects.filter(email=email)

        if usuarios.exists():
            self.add_error('email', 'Email duplicado.')

        return email

    def validate_password_strength(self, valor):
        if len(valor) < 5:
            raise ValidationError('A senha deve ter pelo menos 5 caracteres.')

        #if not any(char.isdigit() for char in valor):
        #    raise ValidationError('A senha deve ter pelo menos 1 dígito.')

        #if not any(char.isalpha() for char in valor):
        #    raise ValidationError('A senha deve ter pelo menos 1 letra.')

class ProfileForm(forms.ModelForm):

    '''

  genero = forms.ChoiceField(choices = Profile.genero_escolhas, widget=forms.Select(attrs={'class' :'form-control'}))
    cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rg = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
    'class': 'form-control'}))
    estado = forms.CharField(max_length=2, widget=forms.TextInput(attrs={
    'id': 'id_estado', 'name': 'estado', 'class': 'form-control'}))
    data_nascimento = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': '1899-01-01'}), initial=datetime.date.today)
    link_instagram = forms.URLField(max_length=200, widget=forms.URLInput(attrs={'class': 'form-control'}))
    link_facebook = forms.URLField(max_length=200, widget=forms.URLInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))

    '''





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        widgets = {'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': '1899-01-01', 'max': '2010-12-31'}),
                    'cpf': forms.TextInput(attrs={'class': 'form-control'}),
                   'genero': forms.Select(attrs={'class' :'form-control'}),
                   'rg': forms.TextInput(attrs={'class': 'form-control'}),
                   'cep': forms.TextInput(attrs={'class': 'form-control'}),
                   'link_facebook': forms.URLInput(attrs={'class': 'form-control'}),
                   'estado': forms.TextInput(attrs={'id': 'id_estado', 'name': 'estado', 'class': 'form-control'}),
                   'cidade': forms.TextInput(attrs={'class': 'form-control'}),
                   'telefone': forms.TextInput(attrs={'class': 'form-control'}),
                   'link_instagram': forms.URLInput(attrs={'class': 'form-control'}),
                   }
        fields = ('genero', 'cpf', 'rg', 'cep', 'cidade', 'estado', 'data_nascimento',
                  'link_instagram', 'link_facebook', 'telefone')


