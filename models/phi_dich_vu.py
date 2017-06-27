# -*- coding: utf-8 -*-

from odoo import models, fields


class phi_dich_vu(models.Model):
    _name = 'bms_project.phi_dich_vu'

    ten = fields.Integer("Tên sản phẩm dịch vụ")
    don_vi_tinh = fields.Char("Đơn vị tính")
    gia = fields.Float("Giá thành")
    trang_thai = fields.Boolean("Trạng thái")
    dich_vu = fields.Many2one('bms_project.dich_vu', string="Dịch vụ")
