from odoo import models, fields

class Document(models.Model):
    _name = 'custom_documents.document'
    _description = 'Custom Document'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    company = fields.Many2one('res.company', string='Company', required=True)