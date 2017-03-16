# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import make_purchase_invoice
from frappe.utils.data import flt, today


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
		pi.bill_no = doc.name
		pi.bill_date = today()

		for item in pi.items:
			for source_item in doc.items:
				if source_item.item_code == item.item_code:
					item.update({
						"item_code": source_item.item_code,
						"item_name": source_item.item_name,
						"qty": source_item.qty,
					})


		pi.save()

