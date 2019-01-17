# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rebrandly_integration"
app_title = "Rebrandly Integration"
app_publisher = "Ivan Ray Altomera"
app_description = "A Frappe module in integrating Rebrandly"
app_icon = "octicon octicon-mirror"
app_color = "#f39c12"
app_email = "irayspacii@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rebrandly_integration/css/rebrandly_integration.css"
# app_include_js = "/assets/rebrandly_integration/js/rebrandly_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/rebrandly_integration/css/rebrandly_integration.css"
# web_include_js = "/assets/rebrandly_integration/js/rebrandly_integration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rebrandly_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rebrandly_integration.install.before_install"
# after_install = "rebrandly_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rebrandly_integration.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rebrandly_integration.tasks.all"
# 	],
# 	"daily": [
# 		"rebrandly_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"rebrandly_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rebrandly_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rebrandly_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rebrandly_integration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rebrandly_integration.event.get_events"
# }

