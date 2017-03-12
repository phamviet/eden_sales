# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import update_status


def on_submit(doc, method):
	"""Handle sample item"""
	if frappe.flags.in_import or frappe.flags.in_test:
		return

	if not doc.po_no:
		return

	# update_status("Delivered", doc.po_no)
