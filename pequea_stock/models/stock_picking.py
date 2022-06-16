from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    customer_po = fields.Char(related='sale_id.customer_po',string="Customer PO", store=True)
