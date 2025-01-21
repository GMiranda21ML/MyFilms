from django import forms

class LoginForms(forms.Form):
    nomeLogin = forms.CharField(
        label = "Nome de Login",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'login-box',
                "placeholder":"Ex.: Gabriel Miranda"
            }
        )
    )

    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 60,
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control",
                "placeholder":"Digite sua senha"
            }
        )
    )