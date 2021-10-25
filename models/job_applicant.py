from odoo import models, fields, api, _

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Good'),
    ('2', 'Very Good'),
    ('3', 'Excellent')
]


class JobApplicant(models.Model):
    _name = "ejobs.applicants"
    _description = "Applicants"
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Application ID", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    active = fields.Boolean("Active", default=True)
    applicant_name = fields.Char("Applicant's Name")
    applicant_mobile = fields.Char("Mobile", size=32, store=True)
    applicant_email = fields.Char("Email", size=128, help="Applicant email", store=True)
    applicant_degree = fields.Selection([
        ('bsc', 'BSc'),
        ('msc', 'MSc/MEng'),
        ('phd', 'PhD')], string='Highest degree',
        copy=False, default='bsc', required=True)
    stage_id = fields.Char('Stage', tracking=True, store=True, readonly=False)
    company_id = fields.Many2one('res.company', "Company", store=True, readonly=False, tracking=True)
    recruiter_id = fields.Many2one('res.users', string='Recruiter', tracking=True)
    department_id = fields.Many2one('hr.department', "Department", store=True, readonly=False, tracking=True)
    job_position_id = fields.Many2one('ejobs.positions', "Applied Job", tracking=True, required=True)
    date_open = fields.Datetime("Assigning date", readonly=True, index=True)
    application_date = fields.Datetime("Application Date", readonly=True, index=True, default=fields.Datetime.now())
    date_closed = fields.Datetime("Closing date", store=True, index=True)
    priority = fields.Selection(AVAILABLE_PRIORITIES, "Priority", default='0')
    salary_proposed = fields.Float("Proposed Salary", tracking=True)
    salary_expected = fields.Float("Expected Salary", tracking=True)
    availability = fields.Date("Availability", tracking=True, required=True)
    color = fields.Integer("Color Index", default=0)
    employee_id = fields.Many2one('hr.employee', string="Employee", help="Employee linked to the applicant.")
    employee_name = fields.Char(related='employee_id.name', string="Employee Name", readonly=False, tracking=True)
    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('done', 'Green'),
        ('blocked', 'Red')], string='Kanban State',
        copy=False, default='normal', required=True)
    medium_find = fields.Selection([
        ('fb', 'Facebook'),
        ('in', 'LinkedIn'),
        ('web', 'Website')], string='Found job via')
    description = fields.Text("Description", tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('ejobs.applicants') or _('New')

        res = super(JobApplicant, self).create(vals)
        return res
