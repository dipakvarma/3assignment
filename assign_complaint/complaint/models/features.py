# * - coding: utf - 8 -
from flectra import api, fields, models

class featuresinfo(models.Model):
    _name = "features.info"

    name = fields.Char(string="Features")
    #product_line = fields.One2many("product.info", "features_id", string="Product")
    product_ids = fields.Many2many("product.info", "product_feature_rel", "feature", "product",
                                    string="Product")