from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)


# class ProfileForm(forms.Form):
#     user = forms.ModelChoiceField(User.objects.all(), required=True)
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}),
#         help_text="How can you describe you in fews worlds...",
#         required=False
#     )
#     web_site = forms.URLField(
#         widget=forms.URLField(attrs={'class': 'form-control'}),
#         label="web site url",
#         help_text="If you are a website, enter the url here...",
#         required=False
#     )
#     avatar = forms.ImageField(
#         upload_to="avatars/",
#         help_text="Select a profile picture !",
#         required=False
#     )
#     signature = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         help_text="Want to add a sign to yous messages ?!",
#         required=False
#     )
#     suscribe_news = forms.CheckboxInput(
#         label="suscribe to news",
#         help_text="Check it if you wish receive some news messages"
#     )
#     address_country = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label="your country name",
#     )
#     address_city = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label="your city name",
#     )
#     address_road = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label="address of the road",
#         required=False
#     )
#     address_zip_code = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label="your zip code",
#         required=False
#     )
