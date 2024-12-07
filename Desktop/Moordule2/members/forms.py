from django.forms import ModelForm
from .models import Members

class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = ["username","nikename","content"]