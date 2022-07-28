def _create_bc_payload(self, bc_order):

    	product_list = []
    	for product in bc_order.products.all():
        	product_options = []
        	if product.product_options:
            	product_options.append(
                	{'id': product.product_options.product_options_id,
                 	'value': product.product_options.value
                	}
            	)
        	if product.product_id:
            	product_list.append({
                    	"product_id": product.product_id,
                    	"product_options": product_options,
                    	"price_inc_tax": product.price_inc_tax,
                    	"price_ex_tax": product.price_ex_tax,
                    	"quantity": product.quantity,
                	})
        	else:
            	product_list.append({
              	"name": product.lineitem_name,
              	"quantity": product.quantity,
              	"price_inc_tax": product.price_inc_tax,
              	"price_ex_tax": product.price_ex_tax,
            	})

    	shipping_list = []
    	for sa in bc_order.shipping_addresses.all():
        	shipping_list.append( {
                	"first_name": sa.first_name,
                	"last_name": sa.last_name,
                	"company": sa.company,
                	"street_1": sa.street_1,
                	"street_2": sa.street_2,
                	"city": sa.city,
                	"state": sa.state,
                	"zip": sa.zip,
                	"country_iso2": sa.country_iso2,
                	"email": sa.email,
                	'shipping_method': sa.shipping_method or ' ',
                	"phone": sa.phone or ' '

            	})

    	payload = {
        	"status_id": bc_order.status_id,
        	"customer_id":  bc_order.customer_id,
        	"billing_address": {
            	"first_name": bc_order.billing_address.first_name,
            	"last_name": bc_order.billing_address.last_name,
            	"street_1": bc_order.billing_address.street_1,
            	"street_2": bc_order.billing_address.street_2,
            	"city": bc_order.billing_address.city,
            	"state": bc_order.billing_address.state or ' ',
            	"zip": bc_order.billing_address.zip or ' ',
            	"country_iso2": bc_order.billing_address.country_iso2,
            	"email": bc_order.billing_address.email,
            	"phone": bc_order.billing_address.phone or ' '
        	},
        	"shipping_addresses": shipping_list,
        	"products": product_list,
        	'date_created': utils.format_datetime(bc_order.date_created) if bc_order.date_created else '',
        	'shipping_cost_ex_tax': bc_order.shipping_cost_ex_tax,
        	'subtotal_ex_tax': bc_order.subtotal_ex_tax,
        	'subtotal_inc_tax': bc_order.subtotal_inc_tax,
        	'total_ex_tax': bc_order.total_ex_tax,
        	'total_inc_tax': bc_order.total_inc_tax,
        	'payment_provider_id': bc_order.payment_provider_id,
        	'staff_notes': bc_order.staff_notes,
        	'refunded_amount': bc_order.refunded_amount,
        	'payment_method': bc_order.payment_method,
        	'discount_amount': bc_order.discount_amount,
        	'external_id': bc_order.external_id,
        	'external_source': bc_order.external_source


    	}
    	return payload
