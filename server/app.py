from flask import Flask, render_template, jsonify
app = Flask(__name__)

data = [
        ("Rick's Subs", "6460 Greenfield Rd", "Dearborn", "Michigan", 48126, "active"),
        ("Orlando's", "1114 Don Juan Valdez Ln", "Taos", "New Mexico", 87571, "inactive"),
        ("Okra's Louisiana Bistro", "9110 Center St", "Manassas", "Virginia", 20110, "inactive"),
        ("Lock & Key Social Drinkery + Kitchen", "11033 Downey Ave", "Downey", "California", 90241, "active"),
        ("Howe restaurant", "5389 IN-9", "Howe", "Indiana", 46746, "active"),
        ("Black Iron Burger", "245 W 38th St", "New York", "New York", 10018, "inactive"),
        ("Merchant Logo DoubleTap KC", "310 Oak St", "Kansas City", "Missouri", 64106, "active"),
        ("The Antler Room", "2506 Holmes St", "Kansas City", "Missouri", 64106, "active"),
        ("Barn Restaurant", "22611 OH-2", "Archbold", "Ohio", 43502, "active"),
        ("Greenhorn", "112 Vine St", "Bluffton", "Ohio", 45817, "inactive"),

    ]

providers = [
        ("Uber"),
        ("DoorDash"),
        ("Waitr"),
    ]

@app.route('/status/<status>/ui')
def get_all_businesses_by_status(status):

    business_list = []

    for business in data:
        if business[5] == status:
            business_list.append(business)

    return render_template("status.html", results=business_list)

@app.route('/status/<status>')
def get_businesses_by_status_data(status):

    business_list = []

    for business in data:
        if business[5] == status:
            business_list.append(business)

    return jsonify(business_list)

@app.route('/businesses')
def get_all_business_data():
    return jsonify(data)
    
@app.route('/businesses-ui')
def get_all_businesses():
    return render_template("businesses.html", data=data)

@app.route('/providers')
def get_all_providers_data():
    return jsonify(providers)
    

@app.route('/providers-ui')
def get_all_providers():

    return render_template("providers.html", data=providers)

