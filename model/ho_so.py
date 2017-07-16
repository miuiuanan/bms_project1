# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ho_so(models.Model):
    _name = 'bms.ho_so'

    file_line = fields.Many2one('ir.attachment')
    ghi_chu = fields.Char()
    id_tai_khoan = fields.One2many('bms.tai_khoan')
    trang_thai = fields.Selection([
        ('chua_hoan_thien', 'truc tiep'),
        ('hoan_thien', 'hoan thien'),
    ], string="trang thai ho so")