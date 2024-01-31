from django import forms
from .models import Appointment, Billing, Inventory, MedicalRecord, Patient,Doctor, Procedure, Operation

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email_address', 'date_of_birth', 'medical_history', 'allergies']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  
            'email_address': forms.EmailInput
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time', 'purpose', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'contact_number', 'email_address']
        widgets = {
            'email_address': forms.EmailInput
        }



class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ['name', 'description', 'duration', 'special_requirements']

class MedicalRecordForm(forms.ModelForm):
    procedure_form = ProcedureForm()  

    class Meta:
        model = MedicalRecord
        fields = ['patient', 'visit_date', 'doctor', 'diagnosis', 'treatment_plan', 'procedure', 'notes']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),  
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity', 'supplier', 'cost']
        widgets = {
            'cost': forms.NumberInput
        }


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'date', 'amount', 'payment_method', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
            'amount': forms.NumberInput,
            'payment_method': forms.RadioSelect(choices=[('1', 'Cash'), ('2', 'Card')])
        }

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['patient', 'date', 'time', 'type', 'status', 'notes', 'doctor']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }


