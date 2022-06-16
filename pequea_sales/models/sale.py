from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    customer_po = fields.Char(string="Customer PO")

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.customer_po:
            invoice_vals.update({
                'customer_po': self.customer_po,
                'sale_order': self.name
            })
        return invoice_vals
