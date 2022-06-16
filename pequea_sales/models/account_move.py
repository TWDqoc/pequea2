from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    customer_po = fields.Char('Customer PO')
    sale_order = fields.Char('Sale Order')
    bill_po_id = fields.Many2one('purchase.order', 'Source Doc Additional')
