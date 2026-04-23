from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date(string='Birth Date')
    assigned_path = fields.Char(string='Assigned Path')
    onboarding_status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Review'),
        ('approved', 'Approved')
    ], string='Onboarding Status', default='draft')
    is_beneficiary = fields.Boolean(string='Is Beneficiary', default=True)
    selected_skills = fields.Text(string='Selected Skills')
    trainee_status = fields.Char(string='Trainee Status')
