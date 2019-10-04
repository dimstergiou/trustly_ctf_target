from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=10,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', max_length=10,
                               widget=forms.TextInput(attrs={'class':'form-control'}))

class ChoiceFieldNoValidation(forms.ChoiceField):
    def validate(self, value):
        pass

class BestCompany(forms.Form):
    COMPANIES = [
        ('tink', 'Tink'),
        ('klarna', 'Klarna'),
        ('izettle', 'iZettle'),
        ('paynova', 'Paynova')
    ]
    company = ChoiceFieldNoValidation(choices=COMPANIES, label='Best FinTech',
                                widget=forms.Select(attrs={'class':'form-control'}))

class CreditCard(forms.Form):
    card = forms.CharField(label='Credit card number', max_length=16,
                           widget=forms.TextInput(attrs={'class':'form-control'}))