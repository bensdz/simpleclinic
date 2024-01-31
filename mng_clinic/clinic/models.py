from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    address = models.CharField(max_length=50)
    medical_history = models.CharField(max_length=50)
    allergies = models.CharField(max_length=50)


class Doctor(models.Model):
    doctor_id = models.IntegerField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, blank = True, null = True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, blank = True, null = True)
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=200)
    status = models.CharField(max_length=50)


class Procedure(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    duration = models.DurationField()
    special_requirements = models.CharField(max_length=50)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    visit_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, blank = True, null = True)
    diagnosis = models.CharField(max_length=50)
    treatment_plan = models.CharField(max_length=50)
    procedure = models.ForeignKey(Procedure, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.CharField(max_length=50)


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class Inventory(models.Model):
    item_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Operation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, blank = True, null = True)




