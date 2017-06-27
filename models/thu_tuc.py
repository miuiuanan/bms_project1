# -*- coding: utf-8 -*-

from odoo import models, fields, api

class thu_tuc(models.Model):
    _name = 'bms_project.thu_tuc'

    ma_dich_vu = fields.Many2one('bms_project.dich_vu', string="Mã dịch vụ")
    ma_tai_khoan = fields.Many2one('bms_project.tai_khoan', string="Mã tài khoản")
    ngay_tao = fields.Date("Ngày tạo")
    tai_lieu = fields.One2Many('bms_project.ho_so', string="Tài liệu")
    ngay_hen_tra = fields.Date("Ngày hẹn trả")
    trangThai = fields.Selection([
        ('nhap', 'nhap'),
        ('sai', 'sai'),
        ('chuan', 'chuan'),
    ], string="Trạng thái")
    trang_thai_thanh_toan = fields.Boolean("Trạng thái thanh toán")