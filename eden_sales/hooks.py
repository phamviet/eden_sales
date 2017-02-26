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
				"Buying Settings-eden_custom",
				"Buying Settings-auto_make_sales_order",
				"Buying Settings-sales_order_customer",
				"Buying Settings-sales_order_company"
			)]
		]
	}

]

doctype_js = {
	"Company": "custom_scripts/company.js",
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/eden_sales/css/eden_sales.css"
# app_include_js = "/assets/eden_sales/js/eden_sales.js"

# include js, css files in header of web template
# web_include_css = "/assets/eden_sales/css/eden_sales.css"
# web_include_js = "/assets/eden_sales/js/eden_sales.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "eden_sales.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "eden_sales.install.before_install"
# after_install = "eden_sales.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "eden_sales.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Purchase Order": {
		"on_submit": [
			"eden_sales.purchase_order.on_submit"
		]
	},
	"Delivery Note": {
		"on_submit": [
			"eden_sales.delivery_note.on_submit"
		]
	},
	"Sales Invoice": {
		"on_submit": [
			"eden_sales.sales_invoice.on_submit"
		]
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"eden_sales.tasks.all"
# 	],
# 	"daily": [
# 		"eden_sales.tasks.daily"
# 	],
# 	"hourly": [
# 		"eden_sales.tasks.hourly"
# 	],
# 	"weekly": [
# 		"eden_sales.tasks.weekly"
# 	]
# 	"monthly": [
# 		"eden_sales.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "eden_sales.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "eden_sales.event.get_events"
# }

