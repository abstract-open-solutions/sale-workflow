# -*- coding: utf-8 -*-
# © 2015 davide.corio@abstract.it
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models

FY_SLOT = '%(fy)s'


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    def _next(self, cr, uid, seq_ids, context=None):
        context = context or {}
        new_seq_ids = []
        #fy_model = self.pool['account.fiscalyear']
        fy_id = context.get('fiscalyear_id', False)
        if fy_id and len(seq_ids) > 1:
            #fy = fy_model.browse(cr, uid, fy_id, context)
            for seq in self.browse(cr, uid, seq_ids, context):
                if (seq.prefix and FY_SLOT in seq.prefix) or (
                        seq.suffix and FY_SLOT in seq.suffix):
                    new_seq_ids.append(seq.id)
        if new_seq_ids:
            seq_ids = new_seq_ids
        return super(IrSequence, self)._next(cr, uid, seq_ids, context)
