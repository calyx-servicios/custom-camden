##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = "res.partner"

    age = fields.Integer(string='Age')
    passport = fields.Integer(string='Passport')
    passport_expiration = fields.Date(string='Passport expiration')
    travel_date = fields.Date(string='Travel date')

    # Assigned Projects/Travels Smart Button
    num_other_projects = fields.Integer(
        compute='_compute_num_other_projects')

    def _compute_num_other_projects(self):
        for partner in self:
            domain = [
                ('partner_id.id', '=', partner.id)]
            partner.num_other_projects = self.env['project.project'].search_count(domain)
