# * - coding: utf - 8 -
from flectra import api, fields, models
from flectra.exceptions import ValidationError

class facultyinfo(models.Model):
    _name = "faculty.info"

    name = fields.Char(string="Name")
    faculty_id = fields.Integer(string="Faculty Id")
    faculty_course = fields.Selection([('science','Science'),('commerce','Commerce'),('arts','Arts')],string="Course")
    faculty_mob_no = fields.Integer(string="Mobile No")

    course_ids = fields.Many2many("course.info", "course1_faculty1_rel", "faculty1", "course1",
                                 string="course")
    _sql_constraints = [('name_uniq','unique(faculty_mob_no)',"mobile number should be unique")]

@api.constrains('faculty_mob_no')
def check_description(self):
        if  self.student_mobile_no < 10:
            raise ValidationError("Mobile number must be 10 digits")
