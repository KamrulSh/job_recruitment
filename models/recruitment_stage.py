from odoo import models, fields, api, _


class RecruitmentStage(models.Model):
    _name = "ejobs.recruitment.stage"
    _description = "Recruitment Stages"
    _order = 'sequence'

    name = fields.Char("Stage Name", required=True, translate=True)
    sequence = fields.Integer("Sequence", default=10)
    requirements = fields.Text("Requirements")
    template_id = fields.Many2one('mail.template', "Email Template")
    legend_blocked = fields.Char(
        'Red Kanban Label', default=lambda self: _('Blocked'), translate=True, required=True)
    legend_done = fields.Char(
        'Green Kanban Label', default=lambda self: _('Ready for Next Stage'), translate=True, required=True)
    legend_normal = fields.Char(
        'Grey Kanban Label', default=lambda self: _('In Progress'), translate=True, required=True)
