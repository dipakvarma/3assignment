# * - coding: utf - 8 -
from flectra import api, fields, models

class doctorinfo(models.Model):
    _name = "doctor.info"

    name = fields.Char(string="Name")
    doctor_specialize = fields.Selection([('urologist','Urologist'),('orthopedic','Orthopedic'),
                                          ('cardiologist','cardiologist'),('dentist','Dentist')])
    patient_line = fields.One2many("patient.info", "doctor_id", string="patient")