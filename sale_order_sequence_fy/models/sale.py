# -*- coding: utf-8 -*-
# © 2015 davide.corio@abstract.it
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def get_fiscal_year(self, cr, uid, date_order):
        fy_model = self.pool['account.fiscalyear']
        fy_id = fy_model.find(cr, uid, date_order)
        return fy_id

    def create(self, cr, uid, vals, context=None):
        context = context or {}
        if 'date_order' in vals and 'fiscalyear_id' not in context:
            fy_id = self.get_fiscal_year(cr, uid, vals['date_order'])
            context.update({'fiscalyear_id': fy_id})
        return super(SaleOrder, self).create(cr, uid, vals, context)
