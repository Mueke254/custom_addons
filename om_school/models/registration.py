from odoo import api, fields, models


class SchoolRegistration(models.Model):
    _name = "school.registration"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Registration"
    student_id = fields.Many2one('school.student', string="student")
    registration_time = fields.Datetime(string='Registration Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date')
    exams = fields.Html(string='Exams')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority", )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True)

    def action_test(self):
        print("Button clicked!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Succesful',
                'type': 'rainbow_man',
            }
        }
