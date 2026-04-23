from odoo import http
from odoo.http import request

class CharityOnboarding(http.Controller):
    @http.route('/charity/onboarding', type='http', auth="public", website=True)
    def onboarding_form(self, **post):
        return request.render('charity_onboarding.onboarding_template')

    @http.route('/charity/onboarding/submit', type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def onboarding_submit(self, **post):
        # منطق حفظ البيانات الأساسي
        partner_vals = {
            'name': post.get('name'),
            'email': post.get('email'),
            'birth_date': post.get('birth_date'),
            'selected_skills': post.get('skills'),
            'is_beneficiary': True,
        }
        request.env['res.partner'].sudo().create(partner_vals)
        return request.render('charity_onboarding.onboarding_thanks')
