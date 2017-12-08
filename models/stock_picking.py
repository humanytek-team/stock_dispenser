# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models, _
from openerp.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    dispenser_user_id = fields.Many2one(
        comodel_name='stock.dispenser',
        string='Dispenser',
        domain=[('is_stock_user', '=', True)])

    user_dispenser_id = fields.Many2one(
        comodel_name='res.users',
        string='User of dispenser',
        compute='_compute_user_dispenser_id',
        store=True)

    env_user_is_stock_manager = fields.Boolean(
        string='Is a stock manager?',
        compute='_compute_is_stock_manager',
        search='_search_env_user_is_stock_manager')

    allow_validate = fields.Boolean(
        string='Allow validate picking',
        compute='_compute_allow_validate')

    def _compute_is_stock_manager(self):
        """ Computes value of field env_user_is_stock_manager """

        for sp in self:
            sp.env_user_is_stock_manager = self.user_has_groups(
                'stock.group_stock_manager')

    def _search_env_user_is_stock_manager(self, operator, value):
        """ Computes the search operation in field env_user_is_stock_manager"""

        stock_picking_ids = list()
        env_user_is_stock_manager = self.user_has_groups(
            'stock.group_stock_manager')
        if env_user_is_stock_manager:
            stock_picking_ids = self.search([]).mapped('id')
        return [('id', 'in', stock_picking_ids)]

    @api.depends('dispenser_user_id')
    def _compute_user_dispenser_id(self):
        """ Computes value of field user_dispenser_id. """

        for picking in self:
            picking.user_dispenser_id = picking.dispenser_user_id.user_id

    @api.depends('env_user_is_stock_manager')
    def _compute_allow_validate(self):
        """ Computes value of field allow_validate. """

        for sp in self:

            if sp.env_user_is_stock_manager:
                sp.allow_validate = True

            else:
                if sp.user_dispenser_id == self.env.user:
                    sp.allow_validate = True

    @api.multi
    def do_new_transfer(self):

        for pick in self:
            if not pick.allow_validate and pick.picking_type_code == 'outgoing':
                raise ValidationError(
                    _('Does not have permission to validate this transfer, is assigned to another dispenser.')
                )

        return super(StockPicking, self).do_new_transfer()
