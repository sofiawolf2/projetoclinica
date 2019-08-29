from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from roles.models import ClinicUser, Patient


class ClinicUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ClinicUser
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ClinicUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = ClinicUser
        fields = ('email', 'password', 'is_patient', 'is_doctor', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ClinicUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = ClinicUserChangeForm
    add_form = ClinicUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin  
    # that reference specific fields on auth.User.
    list_display = ('email', )
    list_filter = ('is_admin', 'is_doctor', 'is_patient')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_doctor', 'is_patient')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



class PatientCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ['email', 'rg', 'cpf']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        patient = super().save(commit=False)
        patient.set_password(self.cleaned_data["password1"])
        patient.is_patient = True
        if commit:
            patient.save()
        return patient


class PatientAdmin(admin.ModelAdmin):
    #form = PatientCreationForm
    add_form = PatientCreationForm

    list_display = ('email', 'rg', 'cpf')
    fieldsets = (
        ('Informções', {'fields': ('email', 'password', 'rg', 'cpf')}),
    )

    search_fields = ('email', 'rg', 'cpf')
    ordering = ('email',)
    filter_horizontal = ()

