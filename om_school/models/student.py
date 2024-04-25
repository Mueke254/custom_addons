from odoo import api,fields,models



class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "School Student"

    name = fields.Text(string='Name', tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    grade = fields.Integer(string='Grade', tracking=True)
    course = fields.Char(string='Course', tracking=True)
    admissionnumber = fields.Integer(string='ADM NO', tracking=True)
    phonenumber = fields.Integer(string='Phone No', tracking=True)
    level = fields.Selection([('certificate', 'Certificate'), ('diploma', 'Diploma'), ('degree', 'Degree')],
                             string="Level", tracking=True)
    active = fields.Boolean(string="Active", default=True)
