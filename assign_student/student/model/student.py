# * - coding: utf - 8 -
from flectra import api, fields, models
from flectra.exceptions import ValidationError



class studentinfo(models.Model):
    _name = "student.info"



    name = fields.Char(string="Student name")
    student_roll_no = fields.Integer(string="Roll No")
    student_gender = fields.Selection([('boy','Boy'),('girl','Girl')],string="Gender", default='boy')
    student_mobile_no = fields.Integer(string="Mobile No")
    student_admission_date = fields.Date(string='Date')
    courses_id = fields.Many2one("course.info", string="select course")

    state = fields.Selection([('success', 'Success'),('pending', 'Pending'),('cancel','Cancel')])

    @api.constrains('student_mobile_no')
    def check_description(self):
        if  self.student_mobile_no < 10:
            raise ValidationError("Mobile number must be 10 digits")

    def student_success(self):
        self.state = "success"

    def student_pending(self):
        self.state = "pending"

    def student_cancel(self):
        self.state = "cancel"