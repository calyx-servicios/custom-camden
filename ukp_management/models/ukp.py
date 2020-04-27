from odoo import models, fields


class PartnerUKP(models.Model):
    _name = 'ukp'
    _rec_name = 'ukp_id'

    def _default_ukp_last_value(self):
        ukp_value = self.env['ukp'].search([])[-1]
        return ukp_value.ukp_id + 1

    ukp_id = fields.Integer(string='UKP Identification', default=_default_ukp_last_value)
