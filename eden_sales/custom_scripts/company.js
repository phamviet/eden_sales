frappe.ui.form.on("Company", {
    onload: function (frm) {
        frm.get_field('default_retail_company').get_query = function () {
            return {
                filters: {domain: "Retail"}
            };
        };
    }
});
