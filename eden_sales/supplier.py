# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe


@frappe.whitelist()
def get_company_stand_for(supplier_name):
	return frappe.get_value("Supplier", supplier_name, "company_stand_for")
