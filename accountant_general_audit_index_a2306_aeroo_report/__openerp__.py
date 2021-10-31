# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author/
{
    "name": "General Audit Index A.230.6 Aeroo Report",
    "version": "8.0.1.0.0",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "depends": [
        "accountant_general_audit_index_a2306",
        "report_aeroo",
        "base_print_policy",
    ],
    "data": [
        "reports/report_general_audit_index_a2306.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}
