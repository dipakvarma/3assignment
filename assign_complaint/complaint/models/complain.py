# * - coding: utf - 8 -
from flectra import api, fields, models

class complaininfo(models.Model):
    _name = "complain.info"

    name = fields.Char(string="Complain")
    #customer_line = fields.One2many("customer.info", "complain_id", string="Customer")
    customer_ids = fields.Many2many("customer.info", "customer_complain_rel", "complain", "customer",
                                    string="Customer")