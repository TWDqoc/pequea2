
from odoo import models, fields, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    @api.depends('production_id', 'production_id.move_raw_ids')
    def _get_raw_material_product(self):
        for rec in self.filtered(lambda l: l.production_id):
            if rec.production_id.move_raw_ids:
                rec.mrp_raw_material_product_id = rec.production_id.move_raw_ids[0].product_id.id
            else:
                rec.mrp_raw_material_product_id = False

    mrp_raw_material_product_id = fields.Many2one('product.product', string="Material",
        compute="_get_raw_material_product", store=True)
