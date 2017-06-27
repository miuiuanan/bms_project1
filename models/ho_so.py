# -*- coding: utf-8 -*-

from odoo import models, fields


class ho_so(models.Model):
    _name = 'bms_project.ho_so'

    ten = fields.Char("Tên tài liệu")
    file = fields.Many2many(
        'ir.attachment',
        string='File tài liệu')
    loai_tai_lieu = fields.Selection([
        ('Tai lieu1', 'Tai lieu 1'),
        ('Tai lieu 2', 'Tai lieu 2'),
    ], string="Loại tài liệu")
    ngay_tao = fields.Date("Ngày tạo")
    chu_so_huu = fields.Integer("Chủ sở hữu ")
    ghi_chu = fields.Char("Ghi chú của cán bộ")
    trang_thai = fields.Boolean("Trạng thái", default=True)
