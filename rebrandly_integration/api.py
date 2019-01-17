import frappe
import json
import requests

@frappe.whitelist()
def create_link(domain, destination):

    apikey = frappe.db.get_single_value('Rebrandly Settings', 'api_key')

    data = {
        'domain': {'fullName': domain},
        'destination': destination
    }

    headers = {
        'Content-type': 'application/json',
        'apikey': apikey
    }

    r = requests.post('https://api.rebrandly.com/v1/links', data=json.dumps(data), headers=headers)

    if r.status_code == requests.codes.ok:
        return {'success': True}
