from odoo import models, fields, api
from odoo.exceptions import ValidationError 
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('list_price')
    def _check_zero_price(self):
        for product in self:
            if product.list_price == 0:
                raise ValidationError('Products priced at 0€ cannot be published for sale.')