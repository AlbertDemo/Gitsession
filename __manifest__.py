{
    "sequence": 1,
    "name": "Yoder Multi-Check Printing",
    "version": "1.0.43",
    "category": "Accounting/Payments",
    "summary": "Print multiple checks per page to optimize check paper usage",
    "description": """
    This module extends the check printing functionality in Odoo to support printing multiple checks per page:
    - Configure to print up to 3 checks per page
    - Optimizes check paper usage
    - Maintains correct check numbering across multiple pages
    - Supports partial page printing with options for handling remaining space
    - Compatible with existing check printing workflows
    """,
    "author": "Yoder Connections",
    "website": "https://www.yoderconnections.com",
    "license": "OPL-1",
    "depends": [
        "base",
        "account",
        "account_accountant",
        "account_check_printing",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
        "wizard/print_multi_checks_views.xml",
        "report/multi_check_report.xml",
        "report/print_multi_check_3up.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "yoder_multi_check/static/src/scss/multi_check_report.scss",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
