# -*- coding: utf-8 -*-

from odoo import models, fields, api

class yeu_cau(models.Model):
    _name = 'bms_project.yeu_cau'

    ma_thu_thu_tuc = fields.Integer("Mã thủ tục")
    san_pham_dich_vu = fields.One2many('bms_project.phi_dich_vu', string="Sản phẩm dịch vụ")
    so_luong = fields.Integer("Số lượng")
    chi_phi_van_chuyen = fields.Float("Chi phí vận chuyển")
    phuong_thuc_nhan = fields.Integer("Phương thức nhận")