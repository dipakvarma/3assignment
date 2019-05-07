# * - coding: utf - 8 -
from flectra import api, fields, models

class productinfo(models.Model):
    _name = "product.info"

    name = fields.Char(string="Name")
    product_image = fields.Binary(string="Image")
    product_price = fields.Integer(string="Price")

    #features_id = fields.Many2one("features.info", string="Features")
    customer_id = fields.Many2one("customer.info", string="Customer")
    features_ids = fields.Many2many("features.info", "product_feature_rel", "product", "feature",string="Feature")