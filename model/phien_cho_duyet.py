# -*- coding: utf-8 -*-

from odoo import models, fields, api

class phien_cho_duyet(models.Model):
    _name = 'bms.phien_cho_duyet'

    ten = fields.Char()
    trang_thai = fields.Selection([
        ('cho_duyet', 'cho duyet'),
        ('da_duyet', 'da duyet'),
    ], string="Trạng thái")
    id_tai_khoan = fields.Many2one('bms.tai_khoan')
    id_ho_so = fields.Many2one('bms.ho_so')
    id_dich_vu = fields.Many2one('bms.dich_vu')
