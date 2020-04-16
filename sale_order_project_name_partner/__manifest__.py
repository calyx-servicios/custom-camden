# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Order Partner as Project Name ",
    "summary": "This module creates a Project (when the product is a service and Project creation is selected)\
    with the Partner as Project Name, instead of the Sale Order Name.",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "category": "Project",
    "website": "http://www.calyxservicios.com.ar",
    "author": "Calyx",
    "maintainers": ["FedericoGregori"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "preloadable": True,
    "depends": [
        "base",
        "sale",
        "project",
        "sale_timesheet"
    ],
}