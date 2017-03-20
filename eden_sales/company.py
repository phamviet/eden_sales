# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe


@frappe.whitelist()
def get_by_customer(customer_name):
	return frappe.get_value("Company", {"customer_profile": customer_name})
