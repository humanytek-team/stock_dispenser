# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models


class StockDispenser(models.Model):
    """ A stock.dispenser record models an Odoo user of group
    stock.group_stock_user and is in charge of dispatching delivery pickings.
    """
    _inherits = {
        'res.users': 'user_id',
    }
    _name = "stock.dispenser"
    _description = 'Stock Dispensers'

    user_id = fields.Many2one(
        'res.users', 'User', ondelete='cascade', required=True)
    stock_picking_ids = fields.One2many(
        'stock.picking', 'dispenser_user_id', 'Stock pickings')
    active_and_free = fields.Boolean('Recently activated and free')

    @api.model
    def create(self, vals):
        new_dispenser = super(StockDispenser, self).create(vals)
        group_stock_user = self.env.ref('stock.group_stock_user')

        if group_stock_user:
            new_dispenser.groups_id += group_stock_user

        return new_dispenser

    @api.multi
    def unlink(self):
        users = self.mapped('user_id')
        result_unlink = super(StockDispenser, self).unlink()

        if result_unlink:
            partners = users.mapped('partner_id')
            users.unlink()
            partners.unlink()

        return result_unlink
