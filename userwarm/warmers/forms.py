from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


# The key difference is the fields attribute,
# which determines the fields that’ll be included in the form. 
# Yiour custom form will use all the fields from UserCreationForm
# and will add the email field