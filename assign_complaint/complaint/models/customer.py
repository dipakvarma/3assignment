# * - coding: utf - 8 -
from flectra import api, fields, models

class customerinfo(models.Model):
    _name = "customer.info"

    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="Mobile No")

    product_line = fields.One2many("product.info", "customer_id", string="Product")

    #complain_id = fields.Many2one("complain.info", string="complain")
    complain_ids = fields.Many2many("complain.info", "customer_complain_rel", "customer", "complain",
                                   string="Complain")