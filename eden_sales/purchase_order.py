# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from frappe.utils.data import add_days


def on_submit(doc, method):
	"""Auto create Sales Order"""
	if frappe.flags.in_import or frappe.flags.in_test:
		return

	buying_settings = frappe.get_doc("Buying Settings")

	if not buying_settings.auto_make_sales_order:
		return

	so = frappe.new_doc("Sales Order")
	so.company = buying_settings.sales_order_company
	so.customer = buying_settings.sales_order_customer
	so.delivery_date = add_days(None, 10)
	so.po_no = doc.name

	for item in doc.get("items"):
		so.append("items", {
			"item_code": item.item_code,
			"qty": item.qty,
			"rate": item.rate,
			"delivered_by_supplier": item.delivered_by_supplier,
			"conversion_factor": item.conversion_factor
		})

	so.submit()

def make_sales_order(**args):
	so = frappe.new_doc("Sales Order")
	args = frappe._dict(args)
	# so.currency = args.currency or "INR"

	so.delivery_date = add_days(None, 10)


def make_from_po():
	po = frappe.get_doc("Purchase Order", "PO-00005")
	on_submit(po, "on_submit")