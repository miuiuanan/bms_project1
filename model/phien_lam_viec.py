# -*- coding: utf-8 -*-

from odoo import models, fields, api

class phien_lam_viec(models.Model):
    _name = 'bms.phien_lam_viec'

    ten = fields.Char(string="")
    phuong_thuc_nhan = fields.fields.Selection([
        ('truc_tiep', 'truc tiep'),
        ('gui_buu_dien', 'gui buu dien'),
    ], string="phuong thuc nhan")
    dia_chi_nhan = fields.Char
    tong_chi_phi = fields.Float
    ma_thanh_toan = fields.Char
    trang_thai_thanh_toan = fields.Boolean("Trạng thái thanh toán")
    trang_thai_plv = fields.Selection([
        ('nhap', 'nhap'),
        ('sai', 'sai'),
        ('chuan', 'chuan'),
    ], string="Trạng thái")

    ma_dich_vu = fields.One2many('bms_project.dich_vu', string="Mã dịch vụ")
    ma_tai_khoan = fields.Many2one('bms_project.tai_khoan', string="Mã tài khoản")
