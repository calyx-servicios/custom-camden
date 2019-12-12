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