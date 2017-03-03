# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe


def set_missing_values(doc, method):
	if not doc.po_no:
		return

	original_company = frappe.get_value("Purchase Order", doc.po_no, "company")
	customer_profile = frappe.get_value("Company", original_company, "customer_profile")

	if not customer_profile:
		frappe.throw("Customer profile is mandatory for company <strong>{}</strong>".format(original_company))

	customer = frappe.get_doc("Customer", customer_profile)
	doc.customer = customer_profile
	doc.customer_name = customer.customer_name

	doc.customer_address = frappe.get_value("Address", {"customer": doc.customer_name, "is_primary_address": 1})

	default_price_list = frappe.get_value("Customer", customer_profile, "default_price_list")
	if default_price_list:
		doc.selling_price_list = default_price_list

