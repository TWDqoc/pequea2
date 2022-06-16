# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _prepare_invoice(self):
        """Prepare the dict of values to create the new invoice for a purchase order.
        """
        res = super(PurchaseOrder, self)._prepare_invoice()
        if res.get('move_type') and res.get('move_type') == 'in_invoice':
            res.update({'bill_po_id': self.id})
        return res
