# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tai_lieu(models.Model):
    _name = 'bms.tai_lieu'

    ten = fields.Char()
    file = fields.Binary()
    loai_tai_lieu = fields.Selection([
        ('blank', 'tai lieu rong'),
        ('tai_lieu_mau', 'tai lieu mau'),
    ], string="tai lieu")