# * - coding: utf - 8 -
from flectra import api, fields, models

class patientinfo(models.Model):
    _name = "patient.info"

    name = fields.Char(string="Name")
    patient_age = fields.Integer(string ="Age")
    patient_mobile_no = fields.Integer(string="Mobile No")
    patient_disease_type = fields.Char(string="Disease Type")

    doctor_id = fields.Many2one("doctor.info", string="Doctor")

    disease_ids = fields.Many2many("disease.info", "doctor_patient_rel", "patient", "disease",
                                   string="disease")