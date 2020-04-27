from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.depends('partner_id')
    def _compute_ukp_ids(self):
        for record in self:
            record.ukp_ids = record.partner_id.ukp_ids

    ukp_ids = fields.Many2many(
        'ukp', string='UKP Identifications', compute='_compute_ukp_ids', store=True)

    ukp_id_to_group_by = fields.Integer(related='ukp_ids.ukp_id', store=True, string='UKP ID to group')