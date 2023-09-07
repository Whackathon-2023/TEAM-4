import csv
from shipping import Shipping
from flask import Flask, jsonify, render_template, request, send_from_directory
from generate_table import dashboard
app = Flask(__name__)

# Define a context processor function
@app.context_processor
def common_data():
    # Define the common data here
    title = 'See Shore'
    description = 'A prediction tool designed to estimate arrival of fertiliser-carrying vessels.'

    # Return the data as a dictionary
    return {'title': title, 'description': description}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/map')
def map_page():
    return render_template('map.html')

# Define an endpoint to retrieve the object
@app.route('/get_object', methods=['GET'])
def get_object():
    obj = Shipping()
    obj.make_table()
    obj.json_form()

    return jsonify(obj.table)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/analyse')
def analyse():
    return render_template('analyse.html')

@app.route('/analyse/lookup/<string:id>')
def lookup(id):
    # Pass the 'id' parameter to the template
    return render_template('search.html', id=id)

@app.route('/get_dash_data')
def get_dash_data():
    d = dashboard()
    return d.generate_data(100)
    

@app.route('/static/config.json')
def get_config_json():
    return send_from_directory('./', 'config.json')

@app.route('/api/get_ships', methods=['GET'])
def get_ships():
    agency_names = request.args.get('AgencyNames')

    if not agency_names:
        return jsonify({'error': 'AgencyNames parameter is missing'}), 400

    agency_names = agency_names.split(',')  # Split the comma-separated list into a Python list

    ship_mapping = {}  # Use a dictionary to map agencies to ships

    file_path = 'data/expected-movement.csv'  # Updated file path

    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Agency'] in agency_names:
                agency = row['Agency']
                ship = row['Ship']
                if agency in ship_mapping:
                    ship_mapping[agency].append(ship)
                else:
                    ship_mapping[agency] = [ship]

    return jsonify({'AgencyShipMapping': ship_mapping})


@app.route('/api/get_ports_visited', methods=['GET'])
def get_ports_visited():
    vessel_name = request.args.get('VesselName')

    if not vessel_name:
        return jsonify({'error': 'VesselName parameter is missing'}), 400

    try:
        with open('data/Vessels-To-Ports-mockdata.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        vessels = data.get('vessels', [])

        for vessel in vessels:
            if vessel.get('Vessel Name') == vessel_name:
                ports_visited = vessel.get('Ports Visited', [])
                return jsonify({'VesselName': vessel_name, 'PortsVisited': ports_visited})

        return jsonify({'error': f'Vessel "{vessel_name}" not found'}), 404

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run()

