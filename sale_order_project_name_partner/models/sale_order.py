from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _timesheet_find_project(self):
        project = super()._timesheet_find_project()
        project.name = project.partner_id.display_name + " {}".format(project.name)
        return project
