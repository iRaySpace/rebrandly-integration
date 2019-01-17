// Copyright (c) 2019, Ivan Ray Altomera and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rebrandly Settings', {
	init_buttons: function(frm) {
		frm.add_custom_button(__('Create Link'), function() {
			var fields = [
				{'fieldname': 'domain', 'fieldtype': 'Link', 'label': 'Domain', 'options': 'Rebrandly Domain', 'reqd': 1},
				{'fieldname': 'destination', 'fieldtype': 'Data', 'label': 'Destination', 'reqd': 1},
			];

			frappe.prompt(fields, (values) => create_new_link(values), 'Create Link', 'Submit');
		});
	},
	refresh: function(frm) {
		frm.trigger('init_buttons');
		var icons = {
			'active': '<i class="octicon octicon-issue-closed text-success"></i>'
		};

		var template = '<table class="table table-condensed table-bordered">\
				<thead>\
					<tr class="text-center">\
						<th>&nbsp;</th>\
						<th>{{ __("Title") }}</th>\
						<th>{{ __("Status") }}</th>\
						<th>{{ __("Short URL") }}</th>\
					</tr>\
				</thead>\
				<tbody>\
				{% for (var i in rows) { %}\
					{% var row = rows[i]; %}\
					<tr>\
						<th class="text-right">{{ parseInt(i) + 1 }}</th>\
						<td>{{ row.title }}</td>\
						<td class="text-center">{{ icons[row.status] }}</td>\
						<td>{{ row.shortUrl }}</td>\
					</tr>\
				{% } %}\
				</tbody>\
			</table>';

		frm.fields_dict.links_html.$wrapper.empty();
		if (frm.doc.links && frm.doc.links.length) {
            $(frappe.render(template, {
                rows: JSON.parse(frm.doc.links),
                icons: icons
            })).appendTo(frm.fields_dict.links_html.$wrapper);
        }

	}
});

function create_new_link(values) {
	frappe.call({
		method: 'rebrandly_integration.api.create_link',
		freeze: true,
		freeze_msg: 'Creating Rebrandly Link',
		args: {
			'domain': values.domain,
			'destination': values.destination
		},
		callback: function(r) {
			if (r.message && r.message.success) {
				frappe.msgprint('Successfully created Rebrandly Link. Save the document to reload the data.');
			}
		}
	});
};
