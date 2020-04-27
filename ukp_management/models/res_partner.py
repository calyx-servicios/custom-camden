from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    ukp_ids = fields.Many2many(
        'ukp', string='UKP Identifications', store=True)

    ukp_id_to_group_by = fields.Integer(related='ukp_ids.ukp_id', store=True, string='UKP ID to group')
