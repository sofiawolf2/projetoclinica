from django.contrib import admin
from roles.models import ClinicUser, Patient
from roles.forms import ClinicUserAdmin, PatientAdmin
from django.contrib.auth.models import Group
# Now register the new UserAdmin...
admin.site.register(ClinicUser, ClinicUserAdmin)
admin.site.register(Patient, PatientAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)