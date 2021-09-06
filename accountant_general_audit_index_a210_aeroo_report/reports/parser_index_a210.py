from openerp.report import report_sxw


class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.context = context
        self.localcontext.update(
            {
                "get_base_amount": self._get_base_amount,
            }
        )

    def _get_base_amount(self, value):
        self.base = ""
        if value == "total_asset":
            self.base = "Total Asset"
        if value == "net_asset":
            self.base = "Net Asset"
        if value == "revenue":
            self.base = "Revenue"
        if value == "cost_of_revenue":
            self.base = "Cost of Revenue"
        if value == "ebt":
            self.base = "EBT"
        if value == "ebitda":
            self.base = "EBITDA"
        if value == "total_liability":
            self.base = "Total Liability"
        if value == "other_base_amount":
            self.base = "Other Base Amount"
        return self.base
