# -*- coding: utf-8 -*-
from odoo import http

class BmsProject(http.Controller):
    @http.route('/bms_project/bms_project/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/bms_project/bms_project/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bms_project.listing', {
            'root': '/bms_project/bms_project',
            'objects': http.request.env['bms_project.bms_project'].search([]),
        })

    @http.route('/bms_project/bms_project/objects/<model("bms_project.bms_project"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bms_project.object', {
            'object': obj
        })