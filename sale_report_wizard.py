from odoo import models, fields, api

class SaleReportWizard(models.TransientModel):
    _name = 'sale.report.wizard'

    from_date = fields.Date(string='From Date', required=True)
    to_date = fields.Date(string='To Date', required=True)
    customer = fields.Many2one('res.partner', string='Customer', domain="[('customer', '=', True)]")

    def generate_report(self):
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'customer_id': self.customer.id,
        }
        return self.env['report'].get_action(self, 'custom_sales_report.sale_report', data=data)
