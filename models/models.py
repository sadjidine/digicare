# -*- coding: utf-8 -*-

########################################################
#    Author : Salifou OMBOTIMBE - salaisse@gmail.com   #
########################################################

# from odoo import models, fields, api


# class digicare(models.Model):
#     _name = 'digicare.digicare'
#     _description = 'digicare.digicare'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

