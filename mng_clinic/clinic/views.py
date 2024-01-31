from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Billing, Inventory, MedicalRecord, Operation, Patient
from .forms import BillingForm, InventoryForm, MedicalRecordForm, OperationForm, PatientForm, ProcedureForm  
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Appointment
from .forms import AppointmentForm  
from .models import Doctor
from .forms import DoctorForm


#HOME PAGE
def homepage(request):
    return render(request, 'homepage.html')


#Patient
class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'
    context_object_name = 'patient'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient       
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')


#Appointment
    
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')

#Doctors
    
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctor'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor_list')

#MedicalRecord
    
class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'medicalrecords/medicalrecord_detail.html'
    context_object_name = 'medicalrecord'

class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medicalrecords/medicalrecord_list.html'
    context_object_name = 'medicalrecords'


class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'
    success_url = reverse_lazy('medicalrecord_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['procedure_form'] = ProcedureForm()
        return context

    def form_valid(self, form):
        if 'submit_record' in self.request.POST:
            # Handle MedicalRecord form submission
            return super().form_valid(form)
        elif 'submit_procedure' in self.request.POST:
            # Handle Procedure form submission
            procedure_form = ProcedureForm(self.request.POST)
            if procedure_form.is_valid():
                procedure = procedure_form.save()
                medical_record = form.save(commit=False)
                medical_record.procedure = procedure
                medical_record.save()
                return redirect(self.success_url)
            else:
                return self.form_invalid(form)
        else:
            return super().form_valid(form)

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medicalrecords/medicalrecord_form.html'
    success_url = reverse_lazy('medicalrecord_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['procedure_form'] = ProcedureForm()
        return context

    def form_valid(self, form):
        if 'submit_record' in self.request.POST:
            # Handle MedicalRecord form submission
            return super().form_valid(form)
        elif 'submit_procedure' in self.request.POST:
            # Handle Procedure form submission
            procedure_form = ProcedureForm(self.request.POST)
            if procedure_form.is_valid():
                procedure = procedure_form.save()
                medical_record = form.save(commit=False)
                medical_record.procedure = procedure
                medical_record.save()
                return redirect(self.success_url)
            else:
                return self.form_invalid(form)
        else:
            return super().form_valid(form)
        
class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = 'medicalrecords/medicalrecord_confirm_delete.html'
    success_url = reverse_lazy('medicalrecord_list')


# Inventory
        
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'    

class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm  
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory_list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm  
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory_list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')


#Billing
    
class BillingListView(ListView):
    model = Billing
    template_name = 'billings/billing_list.html'

class BillingCreateView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billings/billing_form.html'
    success_url = reverse_lazy('billing_list')

class BillingUpdateView(UpdateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billings/billing_form.html'
    success_url = reverse_lazy('billing_list')

class BillingDeleteView(DeleteView):
    model = Billing
    template_name = 'billings/billing_confirm_delete.html'
    success_url = reverse_lazy('billing_list')

#Operations 
    
class OperationsView(View):
    def get(self, request):
        operations = Operation.objects.all()
        return render(request, 'operations/operations.html', {'operations': operations})

class OperationCreateView(CreateView):
    model = Operation
    form_class = OperationForm
    template_name = 'operations/operation_form.html'
    success_url = reverse_lazy('operation_list')

class OperationUpdateView(UpdateView):
    model = Operation
    form_class = OperationForm
    template_name = 'operations/operation_form.html'
    success_url = reverse_lazy('operation_list')

class OperationDeleteView(DeleteView):
    model = Operation
    template_name = 'operations/operation_confirm_delete.html'
    success_url = reverse_lazy('operation_list')

class OperationDetailView(DetailView):
    model = Operation
    template_name = 'operations/operation_detail.html'
    context_object_name = 'operation'

#Billing

class BillingListView(ListView):
    model = Billing
    template_name = 'billings/billing_list.html'

class BillingCreateView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billings/billing_form.html'
    success_url = reverse_lazy('billing_list')

class BillingUpdateView(UpdateView):
    model = Billing
    form_class = BillingForm
    template_name = 'billings/billing_form.html'
    success_url = reverse_lazy('billing_list')

class BillingDeleteView(DeleteView):
    model = Billing
    template_name = 'billings/billing_confirm_delete.html'
    success_url = reverse_lazy('billing_list')

