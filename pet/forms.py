from django import forms

from pet.models import Pet


class PesquisaPetForm(forms.Form):
    query_string = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-secondary', 'max-lenght': '100',
                                      'placeholder': 'Buscar', 'aria-describedby':'button-addon1',
                                      'style':'border-radius: 25px; background-color: var(--blue) !important; color: var(--white)'}, ),
        required=False
    )
    #<input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('nome', 'descricao', 'categoria', 'data_cadastro', 'preco', 'disponivel', 'imagem',
                  'cep', 'raca', 'estado', 'sexo', 'cidade', 'link_facebook', 'telefone', 'link_instagram'
                  ,'data_nascimento')


