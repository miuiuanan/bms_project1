# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dich_vu_con(models.Model):
    _name = 'bms.dich_vu_con'

    id_spdv = fields.One2many('bms.san_pham_dich_vu')
    tong_chi_phi = fields.Float()
    id_dich_vu = fields.Many2one('bms.dich_vu')