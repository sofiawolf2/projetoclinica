from django.contrib import admin
from roles.models import ClinicUser, Paciente, Medico
from roles.forms import ClinicUserAdmin, PatientAdmin, MedicoAdmin
from django.contrib.auth.models import Group
# Now register the new UserAdmin...
admin.site.register(ClinicUser, ClinicUserAdmin)
admin.site.register(Paciente, PatientAdmin)
admin.site.register(Medico,MedicoAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)