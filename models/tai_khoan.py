# -*- coding: utf-8 -*-
from odoo import models, fields


class tai_khoan(models.Model):
    _name = 'bms_project.tai_khoan'

    cmnd = fields.Char("CMND")
    ngay_cap = fields.Date(string='Ngày cấp')
    noi_cap = fields.Char("Nơi cấp")
    email = fields.Char("Email")
    sdt = fields.Char("Số điện thoại")
    ten_co_quan_to_chuc = fields.Char("Tên Cơ quan/Tổ chức")
    dia_chi_co_quan_to_chuc = fields.Char("Địa chỉ Cơ quan/Tổ chức")
    mat_khau = fields.Char("Mật khẩu")
    ngay_tao = fields.Date("Ngày tạo")
    trang_thai = fields.Boolean('Trạng thái', default=True)
    ho_ten = fields.Char("Họ và tên")
