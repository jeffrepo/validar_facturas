#-*- coding: utf-8 -*-
from odoo import models, fields, api, _


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'


    def unlink(self):
        for invoice_attachment in self.filtered(lambda object: object.res_model== 'account.invoice'):
            invoice = self.env['account.invoice'].browse(invoice_attachment.res_id)
            if invoice_attachment.name == invoice.l10n_mx_edi_cfdi_name:
                invoice.l10n_mx_edi_cfdi_name=""
        return super(IrAttachment, self).unlink()



