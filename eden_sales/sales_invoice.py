# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import make_purchase_invoice
from frappe.utils.data import flt


def on_submit(doc, method):
	"""Handle sample item"""
	if frappe.flags.in_import or frappe.flags.in_test:
		return

	item = doc.get("items")[0]
	po_no = None
	if item.sales_order:
		po_no = frappe.get_value("Sales Order", item.sales_order, "po_no")
		if not po_no:
			return

	po = frappe.get_doc("Purchase Order", po_no)
	if flt(po.per_billed, 2) < 100:
		pi = make_purchase_invoice(po_no)
		pi.supplier_sales_invoice = doc.name
		pi.submit()
