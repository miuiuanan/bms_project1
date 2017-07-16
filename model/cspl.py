# -*- coding: utf-8 -*-

from odoo import models, fields


class cspl(models.Model):
    _name = 'bms.cspl'

    # ma_dich_vu = fields.("Mã dịch vụ")
    ten = fields.Char("Tên")
    file = fields.Binary()
    phan_loai = fields.Selection([
        ('tai_lieu', 'tai_lieu'),
        ('thong_tu', 'thong_tu'),
    ], string="Loại cơ sở pháp lý")
    id_dich_vu = fields.Many2many('bms.cspl')