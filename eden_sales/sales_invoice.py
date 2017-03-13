# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import make_purchase_invoice
from frappe.utils.data import flt


def on_submit(doc, method):
	"""Auto make purchase invoice on retail"""

	if frappe.flags.in_import or frappe.flags.in_test:
		return

	from_so = next(d.sales_order for d in doc.items if d.sales_order)
	if not from_so:
		return

	so = frappe.get_doc("Sales Order", from_so)
	if not so.dropship_order or not so.po_no:
		return

	po = frappe.get_doc("Purchase Order", so.po_no)
	if flt(po.per_billed, 2) < 100:
		pi = make_purchase_invoice(po.name)
		pi.supplier_sales_invoice = doc.name
		original_item = pi.items.pop()
		pi.items = []
		for item in doc.items:
			pi.items.append(original_item.update({"qty": item.qty}))

		pi.save()
