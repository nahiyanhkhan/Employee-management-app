from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if Employee.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                "An employee with this phone number already exists."
            )
        return phone


class UpdateEmployeeForm(EmployeeForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields["salary"].widget.attrs["readonly"] = True
        self.fields["designation"].widget.attrs["readonly"] = True


class SearchForm(forms.Form):
    query = forms.CharField(required=False)
