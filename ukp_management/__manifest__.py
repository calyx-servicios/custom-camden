# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "UKP Management",
    "summary": "This Module adds the UKP field for Partners throug CRM, Contacts, Sale Order, Project and Account",
    "version": "11.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Production/Stable",
    "category": "Custom Modules",
    "website": "http://www.calyxservicios.com.ar/",
    "author": "Calyx",
    "maintainers": ["FedericoGregori"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "crm",
        "sale",
        "account",
        "project"
    ],
    "data": [
        "views/ukp_management_assets.xml",
        "views/res_partner.xml",
        "views/crm_lead.xml",
        "views/sale_order.xml",
        "views/account_invoice.xml",
        "views/project_project.xml",
        "views/project_task.xml",
        "views/ukp_management_views.xml"
    ]
}
