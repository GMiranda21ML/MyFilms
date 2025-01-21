from django import forms

class LoginForms(forms.Form):
    nomeLogin = forms.CharField(
        label = "Nome de Login",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "placeholder":"Ex.: Gabriel Miranda",
            }
        )
    )

    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 60,
        widget = forms.PasswordInput(
            attrs = {
                "placeholder":"Digite sua senha",
            }
        )
    )


class CadastroForms(forms.Form):
    nomeCadastro = forms.CharField(
        label = "Nome de cadastro",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "placeholder":"Ex.: Gabriel Miranda",
            }
        )
    )

    email = forms.EmailField(
        label = "Email",
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                "placeholder":"Ex.: gabrielmiranda@xpto.com",
            }
        )
    )

    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 60,
        widget = forms.PasswordInput(
            attrs = {
                "placeholder":"Digite sua senha",
            }
        )
    )

    senhaConfirmada = forms.CharField(
        label = "Confirmação de senha",
        required = True,
        max_length = 60,
        widget = forms.PasswordInput(
            attrs = {
                "placeholder":"Digite sua senha mais uma vez",
            }
        )
    )