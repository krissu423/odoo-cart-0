from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('website_published', 'list_price')
    def _check_zero_price(self):
        for product in self:
            if product.list_price == 0 and product.website_published:
                raise ValidationError('Products priced at 0€ cannot be published for sale.')