frappe.provide('eden_sales.po');

frappe.ui.form.on("Sales Invoice", {
    refresh: function (frm) {
        if (frm.doc.docstatus == 1) {
            frm.add_custom_button(__('Send to Company'), function () {
                frappe.call({
                    type: "GET",
                    method: "eden_sales.sales_invoice.lookup_company",
                    args: {
                        name: frm.doc.name
                    },
                    freeze: true,
                    callback: function (r) {
                        if (!r.exc) {
                            if (r.message) {
                                eden_sales.sinv.sendToCompany(frm, r.message);
                            } else {
                                frappe.msgprint(__("No linked company found on customer {0}", [frm.doc.customer]))
                            }
                        }
                    }
                })
            });
        }
    }
});

eden_sales.sinv = {
    sendToCompany: function (frm, company) {
        var dialog = new frappe.ui.Dialog({
            title: __('Send to Company'),
            fields: [
                {
                    fieldname: 'company', label: __('Company'), 'default': company,
                    fieldtype: 'Link', options: 'Company', read_only: 1
                },
                {
                    fieldtype: "Button", label: __("Send"), fieldname: "send"
                }
            ]
        });

        dialog.fields_dict.send.$input.removeClass('btn-default btn-xs');
        dialog.fields_dict.send.$input.addClass('btn-primary btn-sm');
        dialog.fields_dict.send.$input.click(function () {
            var args = dialog.get_values();
            if (!args) return;
            dialog.hide();

            return frappe.call({
                type: "GET",
                method: "eden_sales.sales_invoice.send_to_company",
                args: {
                    name: frm.doc.name
                },
                freeze: true,
                callback: function (r) {
                    if (!r.exc) {
                        var pi = r.message;
                        frappe.show_alert(__('Purchase Invoice {0} created in company {1}',
					['<a href="#Form/Purchase Invoice/'+ pi.name + '">' + pi.name+ '</a>',
                    '<a href="#Form/Company/' + company + '">' + company + '</a>']
                        ));
                    }
                }
            })
        });

        dialog.show();
    }
};
