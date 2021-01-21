# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class Student(models.Model):
    _name = 'student.student'
    _description = "Students"

    name = fields.Char()
    age = fields.Integer()

    # description = fields.Text('Private Note')