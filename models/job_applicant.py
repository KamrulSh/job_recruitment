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
    company_id = fields.Many2one('res.company', "Company", compute='_compute_company', store=True, tracking=True)
    recruiter_id = fields.Many2one('res.users', string='Recruiter', compute='_compute_recruiter', readonly=False, tracking=True)
    department_id = fields.Many2one('hr.department', "Department", compute='_compute_department', store=True,
                                    readonly=False, tracking=True)
    job_position_id = fields.Many2one('ejobs.positions', "Applied Job", tracking=True, required=True)
    date_open = fields.Datetime("Assigning date", readonly=True, index=True)
    application_date = fields.Datetime("Application Date", readonly=True, index=True, default=fields.Datetime.now())
    date_closed = fields.Datetime("Closing date", store=True, index=True)
    priority = fields.Selection(AVAILABLE_PRIORITIES, "Priority", default='0')
    salary_proposed = fields.Float("Proposed Salary", tracking=True)
    salary_expected = fields.Float("Expected Salary", tracking=True)
    availability = fields.Date("Availability", tracking=True, required=True)
    color = fields.Integer("Color Index", default=0)
    kanban_state = fields.Selection([
        ('normal', 'In progress'),
        ('done', 'Ready for next stage'),
        ('blocked', 'Blocked')], string='Kanban State',
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

    @api.depends('job_position_id')
    def _compute_department(self):
        for applicant in self:
            applicant.department_id = applicant.job_position_id.department_id.id

    @api.depends('job_position_id')
    def _compute_company(self):
        for applicant in self:
            applicant.company_id = applicant.job_position_id.company_id.id

    @api.depends('job_position_id')
    def _compute_recruiter(self):
        for applicant in self:
            applicant.recruiter_id = applicant.job_position_id.recruiter_id.id
