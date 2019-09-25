##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class TravelDestination(models.Model):
    _name = "travel.destination"

    name = fields.Char(string="City", size=50, required=True)
    country_id = fields.Many2one('res.country', string='Country')