@app.route('/update_silence_threshold', methods=['POST'])
def update_silence_threshold():
    data = request.json

    if 'silence_threshold' in data:
        try:
            with open('settings.json', 'r') as file:
                settings = json.load(file)
        except FileNotFoundError:
            settings = {}

        settings['silence_threshold'] = data['silence_threshold']

        with open('settings.json', 'w') as file:
            json.dump(settings, file, indent=4)

        return jsonify({"message": "Silence threshold updated successfully"}), 200
    else:
        return jsonify({"error": "Missing silence_threshold in request"}), 400
