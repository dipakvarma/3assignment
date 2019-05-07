# * - coding: utf - 8 -
from flectra import api, fields, models

class courseinfo(models.Model):
    _name = "course.info"

   #@api.depends('student_line')
    #def _compute_total_courses(self):
     #       records = self.env['student.info'].search_count([('courses_id', '=', 'Self.id')])
       #     print("-----------------record-------------", self.id)

    name = fields.Selection([('science', 'Science'), ('commerce', 'Commerce'), ('arts', 'Arts')],
                                   string="Course")
    course_code = fields.Integer(string="Course code")

    student_line = fields.One2many("student.info", "courses_id", string="student list")
    #total_rooms = fields.Integer(string="Total Rooms", compute=_compute_total_courses, store=True)

    faculty_ids = fields.Many2many("faculty.info", "course1_faculty1_rel", "course1", "faculty1",
                                    string="faculty")