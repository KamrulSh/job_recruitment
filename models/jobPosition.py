from odoo import models, fields, api


class JobPositions(models.Model):
    _name = 'ejobs.positions'
    _description = 'Job positions'
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Position Name', required=True, tracking=True)
    description = fields.Char(string='Description', tracking=True)
    company_id = fields.Char(string='Company')
    department_id = fields.Char(string='Department', tracking=True)
    no_of_recruitment = fields.Integer(string='No. of recruitment', tracking=True)
