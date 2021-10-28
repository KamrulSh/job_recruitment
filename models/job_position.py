from odoo import models, fields, api
from odoo.exceptions import ValidationError


class JobPositions(models.Model):
    _name = 'ejobs.positions'
    _description = 'Job positions'
    _order = 'id asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Position Name', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    company_id = fields.Many2one('res.partner', string='Company', tracking=True)
    department_id = fields.Many2one('hr.department', string='Department', tracking=True)
    recruiter_id = fields.Many2one('res.users', string='Recruiter', tracking=True)
    no_of_recruitment = fields.Integer(string='No. of recruitment', tracking=True, required=True)
    is_favorite = fields.Boolean(tracking=True)
    color = fields.Integer("Color Index")
    date_open = fields.Datetime("Job Assigning date", readonly=False, index=True)
    date_closed = fields.Datetime("Job Closing date", store=True, index=True)
    view_applicant_ids = fields.One2many('ejobs.applicants', 'job_position_id', string="Applicants")
    salary_proposed = fields.Float("Proposed Salary", tracking=True, required=True)

    @api.constrains('salary_proposed')
    def _check_salary_proposed(self):
        for record in self:
            if record.salary_proposed <= 0:
                raise ValidationError('Proposed salary must be greater than 0')
