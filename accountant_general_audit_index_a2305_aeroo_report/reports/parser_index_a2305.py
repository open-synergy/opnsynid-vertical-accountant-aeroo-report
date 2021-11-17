from openerp.report import report_sxw


class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.context = context
        self.line_data = []
        self.categ_data = []
        self.localcontext.update(
            {
                "get_category": self._get_category,
                "get_line": self._get_line,
            }
        )

    def _get_category(self, index):
        obj_cat = self.pool.get("accountant.general_audit_relevant_external_factor")
        header = index
        cat_ids = obj_cat.search(
            self.cr, self.uid, [("index_a2305_id.id", "=", header)], order="category_id"
        )
        no = 0
        cek_cat = "x"
        for cat in obj_cat.browse(self.cr, self.uid, cat_ids).sorted(
            key=lambda s: s.category_id.sequence
        ):
            if cek_cat != cat.category_id:
                no += 1
                res = {
                    "no": no,
                    "index": cat.index_a2305_id,
                    "category": cat.category_id,
                }
                self.categ_data.append(res)
            cek_cat = cat.category_id
        return self.categ_data

    def _get_line(self, index, categ):
        self.line_data = []
        obj_line = self.pool.get("accountant.general_audit_relevant_external_factor")
        header = index
        line_ids = obj_line.search(
            self.cr,
            self.uid,
            [("index_a2305_id.id", "=", header), ("category_id.id", "=", categ.id)],
        )
        nomor = 0
        for line in obj_line.browse(self.cr, self.uid, line_ids).sorted(
            key=lambda s: s.external_factor_id.sequence
        ):
            nomor += 1
            res = {
                "nomor": nomor,
                "pemahaman": line.external_factor_id.name,
                "impact": line.impact,
                "account": line.account_type_ids,
            }
            self.line_data.append(res)
        return self.line_data
