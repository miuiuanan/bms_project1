# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dich_vu(models.Model):
    _name = 'bms_project.dich_vu'

    mo_ta = fields.Char("Mô tả")
    ten = fields.Char("Tên dịch vụ")
    phi_dich_vu = fields.One2many('bms_project.phi_dich_vu', string="Phí dịch vụ")
    ngay_tao = fields.Date("Ngày tạo")
    tong_phi = fields.Float("Tổng phí")
    ghi_chu = fields.Char("Notes")
    ma_thanh_toan = fields.Char("Mã thanh toán")