# -*- coding: utf-8 -*-

from odoo import models, fields


class cspl(models.Model):
    _name = 'bms_project.cspl'

    # ma_dich_vu = fields.("Mã dịch vụ")
    ten = fields.Char("Tên")
    ngay_upload = fields.Date("Ngày upload")
    file = fields.Binary(string='Tài liệu chuẩn')
    phan_loai = fields.Selection([
        ('tai_lieu', 'tai_lieu'),
        ('thong_tu', 'thong_tu'),
    ], string="Loại cơ sở pháp lý")
