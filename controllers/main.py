# -*- encoding: utf-8 -*-
import logging
import werkzeug
import odoo
import odoo.modules.registry
import ast

from odoo import http , _
from odoo.http import request, _logger
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.addons.web.controllers.main import Home
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

import datetime
import pytz

class Home(Home):

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        cr = request.cr
        uid = odoo.SUPERUSER_ID
        param_obj = request.env['ir.config_parameter']
        request.params['disable_footer'] = ast.literal_eval(param_obj.get_param('login_form_disable_footer')) or False
        request.params['disable_database_manager'] = ast.literal_eval(param_obj.get_param('login_form_disable_database_manager')) or False

        change_background = ast.literal_eval(param_obj.get_param('login_form_change_background_by_hour')) or False
        if change_background:
            config_login_timezone = param_obj.get_param('login_form_change_background_timezone')
            tz = config_login_timezone and pytz.timezone(config_login_timezone) or pytz.utc
            current_hour = datetime.datetime.now(tz=tz).hour or 10
            
            if (current_hour >= 0 and current_hour < 3) or (current_hour >= 18 and current_hour < 24): # Night
                request.params['background_src'] = param_obj.get_param('login_form_background_night') or ''
            elif current_hour >= 3 and current_hour < 7: # Dawn
                request.params['background_src'] = param_obj.get_param('login_form_background_dawn') or ''
            elif current_hour >= 7 and current_hour < 16: # Day
                request.params['background_src'] = param_obj.get_param('login_form_background_day') or ''
            else: # Dusk
                request.params['background_src'] = param_obj.get_param('login_form_background_dusk') or ''
        else:
            request.params['background_src'] = param_obj.get_param('login_form_background_default') or ''
        return super(Home, self).web_login(redirect, **kw)


class AuthSignup(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()

        if not qcontext.get('token') and not qcontext.get('signup_enabled'):
            raise werkzeug.exceptions.NotFound()

        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_signup(qcontext)
                return super(AuthSignupHome, self).web_login(*args, **kw)
            except (SignupError, AssertionError), e:
                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
                    qcontext["error"] = _("Another user is already registered using this email address.")
                else:
                    _logger.error(e.message)
                    qcontext['error'] = _("Could not create a new account.")

        self.create_account(qcontext)
        return request.render('auth_signup.signup', qcontext)

    # @http.route('/web/reset_password', type='http', auth='public', website=True)
    # def web_auth_reset_password(self, *args, **kw):
    #     qcontext = self.get_auth_signup_qcontext()
    #
    #     if not qcontext.get('token') and not qcontext.get('reset_password_enabled'):
    #         raise werkzeug.exceptions.NotFound()
    #
    #     if 'error' not in qcontext and request.httprequest.method == 'POST':
    #         try:
    #             if qcontext.get('token'):
    #                 self.do_signup(qcontext)
    #                 return super(AuthSignupHome, self).web_login(*args, **kw)
    #             else:
    #                 login = qcontext.get('login')
    #                 assert login, "No login provided."
    #                 request.env['res.users'].sudo().reset_password(login)
    #                 qcontext['message'] = _("An email has been sent with credentials to reset your password")
    #         except SignupError:
    #             qcontext['error'] = _("Could not reset your password")
    #             _logger.exception('error when resetting password')
    #         except Exception, e:
    #             qcontext['error'] = e.message or e.name
    #
    #     return request.render('auth_signup.reset_password', qcontext)

    def get_auth_signup_config(self):
        """retrieve the module config (which features are enabled) for the login page"""

        IrConfigParam = request.env['ir.config_parameter']
        return {
            'signup_enabled': IrConfigParam.sudo().get_param('auth_signup.allow_uninvited') == 'True',
            'reset_password_enabled': IrConfigParam.sudo().get_param('auth_signup.reset_password') == 'True',
        }

    def get_auth_signup_qcontext(self):
        """ Shared helper returning the rendering context for signup and reset password """
        qcontext = request.params.copy()
        qcontext.update(self.get_auth_signup_config())
        if qcontext.get('token'):
            try:
                # retrieve the user info (name, login or email) corresponding to a signup token
                token_infos = request.env['res.partner'].sudo().signup_retrieve_info(qcontext.get('token'))
                for k, v in token_infos.items():
                    qcontext.setdefault(k, v)
            except:
                qcontext['error'] = _("Invalid signup token")
                qcontext['invalid_token'] = True
        return qcontext

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = { key: qcontext.get(key) for key in ('login', 'name', 'password') }
        assert values.values(), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

    def _signup_with_values(self, token, values):
        db, login, password = request.env['res.users'].sudo().signup(values, token)
        request.env.cr.commit()     # as authenticate will use its own cursor we need to commit the current transaction
        uid = request.session.authenticate(db, login, password)
        if not uid:
            raise SignupError(_('Authentication Failed.'))

    def create_account(self,values):

        # this function will create a account and deacvite res.user account and send email
        print "done self.env['ir.sequence'].next_by_code('product.price.serial')"
        value = {key: values.get(key) for key in ('login',
                                                  'name',
                                                  'so_can_cuoc',
                                                  'password',
                                                  'noi_cap',
                                                  'ngay_cap',
                                                  'sdt',
                                                  'ten_cq',
                                                  'dia_chi_cq',
                                                  )}
        user_id = request.env['res.user'].search([])[-1].id
        self.env['bms.tai_khoan'].create({
            'ho_ten': value.get('password'),
            'so_can_cuoc': value.get('so_can_cuoc'),
            'noi_cap': value.get('noi_cap'),
            'ngay_cap': value.get('ngay_cap'),
            'email':value.get('login'),
            'sdt': value.get('sdt'),
            'ten_cq': value.get('ten_cq'),
            'dia_chi_cq': value.get('dia_chi_cq'),
            'mat_khau': value.get('password'),
            'ngay_tao_tk': datetime.datetime.now(),
            'trang_thai': False,
            'user_id': user_id,
        })
        user = self.env['res.user'].search([])[-1]
        user.write({
            'status' : False,
        })

class Confirm_tai_khoan(http.Controller):

    @http.route('/tai_khoan/done/<int:tk_id>', type='http', website=True, auth='public')
    def taikhoan_accept(self, tk_id, email=None, res_id=None, **post):
        rec = request.env['bms.tai_khoan'].sudo().browse(int(tk_id))
        rec.write({'trang_thai': 'True'})
        return "<h3>Tài khoản của bạn đã được kích hoạt thành công!</h3>"

    @http.route('/tai_khoan/cancel/<int:tk_id>', type='http', website=True, auth='public')
    def taikhoan_reject(self, tk_id, email=None, res_id=None, **post):
        rec = request.env['bms.tai_khoan'].sudo().browse(int(tk_id))
        rec.write({'state': 'cancel'})
        return "<h3>Tài khoản đăng ký bằng email của bạn đã bị khoá</h3>"
