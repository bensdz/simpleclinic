from django.contrib import admin

from clinic.models import Operation, Patient,Doctor,Appointment,Procedure,MedicalRecord,Billing,Inventory

admin.site.register(Patient)
admin.site.register(Doctor)
#admin.site.register(PatientFile)
admin.site.register(Appointment)
admin.site.register(Procedure)
admin.site.register(MedicalRecord)
admin.site.register(Billing)
admin.site.register(Inventory)

admin.site.register(Operation)