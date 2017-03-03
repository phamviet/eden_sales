# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry


def on_submit(doc, method):
	"""Handle supplier payment auto creation"""
	if frappe.flags.in_import or frappe.flags.in_test:
		return

	if doc.payment_type == "Pay" and len(doc.references) == 1:
		if any(reference.reference_doctype == "Purchase Invoice" for reference in doc.references):
			reference = doc.references[0]
			supplier_sales_invoice = frappe.get_value("Purchase Invoice", reference.reference_name, "supplier_sales_invoice")
			if not supplier_sales_invoice:
				return

			receive_payment(supplier_sales_invoice)



def receive_payment(supplier_sales_invoice):
	pe = get_payment_entry("Sales Invoice", supplier_sales_invoice)
	pe.paid_to = frappe.db.get_value("Account", {"company": pe.company, "account_type": "Cash"}, "name")
	if not pe.paid_to:
		frappe.throw("Cash account is required for company <strong>{}</strong> to make receive payment entry against this.".format(pe.company))

	pe.flags.ignore_mandatory = True
	pe.save(ignore_permissions=True)

