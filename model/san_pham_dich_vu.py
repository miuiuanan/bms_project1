# -*- coding: utf-8 -*-

from odoo import models, fields


class san_pham_dich_vu(models.Model):
    _name = 'bms_project.san_pham_dich_vu'

    ten = fields.Integer("Tên sản phẩm dịch vụ")
    don_vi_tinh = fields.Char("Đơn vị tính")
    gia = fields.Float("Giá thành")
    # trang_thai = fields.Boolean("Trạng thái")
