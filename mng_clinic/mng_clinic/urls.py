from django.contrib import admin
from django.urls import path

from clinic.views import AppointmentCreateView, AppointmentDeleteView, AppointmentDetailView, AppointmentListView, AppointmentUpdateView, DoctorDeleteView, MedicalRecordDeleteView, OperationCreateView, OperationDeleteView, OperationDetailView, OperationUpdateView, OperationsView, PatientCreateView, PatientDeleteView, PatientListView, PatientUpdateView, InventoryCreateView, InventoryDeleteView, InventoryListView, InventoryUpdateView, MedicalRecordCreateView, MedicalRecordDetailView, MedicalRecordListView, MedicalRecordUpdateView, PatientCreateView, PatientListView,PatientDetailView,PatientUpdateView,DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, homepage
from clinic.views import  BillingListView, BillingCreateView, BillingUpdateView, BillingDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patient/add/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/add/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/add/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor/<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
    path('medicalrecords/', MedicalRecordListView.as_view(), name='medicalrecord_list'),
    path('medicalrecord/<int:pk>/', MedicalRecordDetailView.as_view(), name='medicalrecord_detail'),
    path('medicalrecord/add/', MedicalRecordCreateView.as_view(), name='medicalrecord_create'),
    path('medicalrecord/<int:pk>/edit/', MedicalRecordUpdateView.as_view(), name='medicalrecord_update'),
    path('medical_record/<int:pk>/delete/', MedicalRecordDeleteView.as_view(), name='medical_record_delete'),
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),
     path('Patient/', PatientListView.as_view(), name='Patient_list'),
    path('Patient/create/', PatientCreateView.as_view(), name='Patient_create'),
    path('Patient/update/<int:pk>/', PatientUpdateView.as_view(), name='Patient_update'),
    path('Patient/delete/<int:pk>/', PatientDeleteView.as_view(), name='Patient_delete'),
    path('operations/', OperationsView.as_view(), name='operation_list'),
    path('operation/create/', OperationCreateView.as_view(), name='operation_create'),
    path('operation/update/<int:pk>/', OperationUpdateView.as_view(), name='operation_update'),
    path('operation/delete/<int:pk>/', OperationDeleteView.as_view(), name='operation_delete'),
    path('operations/<int:pk>/', OperationDetailView.as_view(), name='operation_detail'),
    path('billing/', BillingListView.as_view(), name='billing_list'),
    path('billing/add/', BillingCreateView.as_view(), name='billing_create'),
    path('billing/<int:pk>/edit/', BillingUpdateView.as_view(), name='billing_update'),
    path('billing/<int:pk>/delete/', BillingDeleteView.as_view(), name='billing_delete'),
]
