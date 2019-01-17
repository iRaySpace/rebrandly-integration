# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ivan Ray Altomera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

import frappe
import requests
import json


class RebrandlySettings(Document):
	@staticmethod
	def set_rebrandly_link(links):
		frappe.db.sql("""DELETE FROM  `tabRebrandly Link`""")

		for link in links:
			frappe.get_doc({
				'doctype': 'Rebrandly Link',
				'id': link['id'],
				'title': link['title'],
				'short_url': link['shortUrl'],
				'https': link['https'],
				'status': link['status'].title(),
				'destination': link['destination']
			}).insert()

	@staticmethod
	def set_rebrandly_domain(domains):
		frappe.db.sql("""DELETE FROM `tabRebrandly Domain`""")

		for domain in domains:
			frappe.get_doc({
				'doctype': 'Rebrandly Domain',
				'id': domain['id'],
				'full_name': domain['fullName']
			}).insert()

	def validate(self):
		r = requests.get('https://api.rebrandly.com/v1/links', headers={
			'Content-Type': 'application/json',
			'apikey': self.api_key
		})

		if r.status_code == requests.codes.ok:
			RebrandlySettings.set_rebrandly_link(r.json())
			self.links = json.dumps(r.json())

		r = requests.get('https://api.rebrandly.com/v1/domains', headers={
			'Content-Type': 'application/json',
			'apikey': self.api_key
		})

		if r.status_code == requests.codes.ok:
			RebrandlySettings.set_rebrandly_domain(r.json())
