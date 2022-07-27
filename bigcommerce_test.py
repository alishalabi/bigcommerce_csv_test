from dotenv import load_dotenv
load_dotenv()
import os
import requests
import json
import csv

hash2 = os.environ.get("STORE_HASH2")
api_key2 = os.environ.get("API_TOKEN2")

get_url = f"https://api.bigcommerce.com/stores/{hash2}/v2/orders"
headers = {
    "X-Auth-Token": api_key2,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# CSV:
# ['Order ID', 'Customer ID', 'Customer Name', 'Customer Email', 'Customer Phone', 'Order Date', 'Order Status', 'Subtotal (inc tax)', 'Subtotal (ex tax)', 'Tax Total', 'Shipping Cost (inc tax)', 'Shipping Cost (ex tax)', 'Ship Method', 'Handling Cost (inc tax)', 'Handling Cost (ex tax)', 'Store Credit Redeemed', 'Gift Certificate Amount Redeemed', 'Gift Certificate Code', 'Gift Certificate Expiration Date', 'Coupon Details', 'Order Total (inc tax)', 'Order Total (ex tax)', 'Payment Method', 'Total Quantity', 'Total Shipped', 'Date Shipped', 'Order Currency Code', 'Exchange Rate', 'Order Notes', 'Customer Message', 'Billing First Name', 'Billing Last Name', 'Billing Company', 'Billing Street 1', 'Billing Street 2', 'Billing Suburb', 'Billing State', 'Billing Zip', 'Billing Country', 'Billing Phone', 'Billing Email', 'Shipping First Name', 'Shipping Last Name', 'Shipping Company', 'Shipping Street 1', 'Shipping Street 2', 'Shipping Suburb', 'Shipping State', 'Shipping Zip', 'Shipping Country', 'Shipping Phone', 'Shipping Email', 'Product Details', 'Refund Amount', 'Channel ID', 'Channel Name']

def post_order():
    url = "orders.csv"
    f = open(url, "r")
    csv_reader = csv.reader(f)
    for row in csv_reader:
        payload = {
            "id": row[0],
            "customer_id": row[1],
            # "custome_name": row[2],
            "billing_address": {
                "first_name": row[30],
                "last_name": row[31],
                "company": row[32],
                "street_1": row[33],
                "street_2": row[34],
                "suburb": row[35],
                "state": row[36],
                "zip": row[37],
                "country": row[38],
                "phone": row[39],
                "email": row[40]
            },
            "date_created": row[5],
            "status": row[6],
            "subtotal_inc_tax": row[7],
            "subtotal_ex_tax": row[8],
            "total_tax": row[9],
            "shipping_cost_inc_tax": row[10],
            "shipping_cost_ex_tax": row[11],
            # "shipping_method": row[12],
            "handling_cost_inc_tax": row[13],
            "handling_cost_ex_tax": row[14],
            "store_credit_amount": row[15],
            "gift_certificate_amount": row[16],
            # "gift_certificate_code": row[17],
            # "gift_certificate_exp": row[18],
            # "coupons": {
            #     "url": row[19],
            #     "resource": "/orders/128962/coupons"
            #  },
            "subtotal_inc_tax": row[20],
            "subtotal_ex_tax": row[21],
            "payment_method": row[22],
            "items_total": row[23],
            "items_total": row[24],
            "date_shipped": row[25],
            "currency_code": row[26],
            "currency_exchange_rate": row[27],
            "staff_notes": row[28],
            "customer_message": row[29],
            # "shipping_addresses": {
            #     "first_name": row[41],
            #     "last_name": row[42],
            #     "company": row[43],
            #     "street_1": row[44],
            #     "street_2": row[45],
            #     "suburb": row[46],
            #     "state": row[47],
            #     "zip": row[48],
            #     "country": row[49],
            #     "phone": row[50],
            #     "email": row[51]
            # },
            # "products": row[52],
            "refunded_amount": row[53],
            "channel_id": row[54],
            "channel_name": row[55]


        }
        print(payload)
        return
        # if row[0] != "Order ID":
        #     print(row)
        #     return

def get_all():
    r = requests.get(get_url, headers=headers)
    # print(r.text)

    # json_data = json.loads(r.text)
    # print(json_data)

    counter = 0
    for response in r.text:
        counter += 1
        print(response)
        return

    # counter = 0
    # for response in r:
    #     counter += 1
    #
    # print(counter)

# for response in r:
#     decoded = json.dumps(response.decode("utf-8"))
#     print(decoded.id)
# jsonResponse = json.loads(r)
#
# counter = 0
# for response in jsonResponse:
#     print(response.customer_id)

# print(r.__dict__)


# print(dir(r))

# print(my_dict)

# x = requests.get('https://w3schools.com/python/demopage.htm')
#
# print(x.text)

# get_all()
post_order()
