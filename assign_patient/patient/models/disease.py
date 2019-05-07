# * - coding: utf - 8 -
from flectra import api, fields, models

class diseaseinfo(models.Model):
    _name = "disease.info"

    name = fields.Char(string="Disease Name")

    patient_ids = fields.Many2many("doctor.info", "doctor_patient_rel", "disease", "patient",
                                  string="patient")