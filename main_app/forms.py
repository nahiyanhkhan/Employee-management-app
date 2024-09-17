from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class UpdateEmployeeForm(EmployeeForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields["salary"].widget.attrs["readonly"] = True
        self.fields["designation"].widget.attrs["readonly"] = True


class SearchForm(forms.Form):
    query = forms.CharField(required=False)
