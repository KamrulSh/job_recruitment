from odoo import http
from odoo.http import request


class WebApplicant(http.Controller):

    # route for application website
    @http.route('/apply_job', type='http', auth='user', website=True)
    def appointment_webform(self, **kw):
        job_position_rec = request.env['ejobs.positions'].sudo().search([])
        return http.request.render('job_recruitment.apply_job', {
            'job_position_rec': job_position_rec
        })

    @http.route('/create/application', type="http", auth="user", website=True)
    def create_applicant(self, **kw):
        # print("\nData Received.....", kw)
        request.env['ejobs.applicants'].sudo().create(kw)
        return request.render("job_recruitment.user_thanks", {})
