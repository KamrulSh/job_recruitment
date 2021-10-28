from odoo import models, fields, api


class EmployeesInformation(models.Model):
    _inherit = 'hr.employee'
    _description = "Employee Info"
