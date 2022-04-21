from odoo import api, fields, models

class UniversityStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    ref = fields.Char(string="Ref")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    email = fields.Char(string="Email")
    phone = fields.Char(string="¨Phone")
    faculty = fields.Selection([('ntic', 'Faculté de nouvelles technologies'), ('eco', 'Faculté des sciences économiques')], string="Faculty")
    rate = fields.Float(string="Rate")
    establish_date = fields.Date(string="Establish Date")
    active = fields.Boolean(string="Active", default=True)
