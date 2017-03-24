# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "eden_sales"
app_title = "Eden Sales"
app_publisher = "Viet Pham"
app_description = "Eden custom sales workflow"
app_icon = "octicon octicon-diff"
app_color = "grey"
app_email = "inbox@phamviet.net"
app_license = "MIT"

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": [
			["name", "in", (
				"Company-customer_profile",
				"Supplier-company_stand_for",
				"Purchase Invoice-supplier_sales_invoice",
				"Sales Order-dropship_order",
				"Sales Order-dropship_customer_name",
				"Sales Order-dropship_contact",
				"Sales Order-dropship_mobile",
				"Sales Order-dropship_email",
				"Delivery Note-dropship_customer_name",
				"Delivery Note-dropship_contact",
				"Delivery Note-dropship_mobile",
				"Delivery Note-dropship_email",
				"Delivery Note-dropship_order",
				"Sales Order-shipping_customer_section",
			)]
		]
	}

]

doctype_js = {
	"Purchase Order": "scripts/po.js",
	"Sales Invoice": "scripts/sales_invoice.js",
	"Delivery Note": "scripts/delivery_note.js",
}

doc_events = {

	"Sales Order": {
		"set_missing_values": [
			"eden_sales.sales_order.set_missing_values"
		]
	}
}
