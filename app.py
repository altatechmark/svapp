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



@app.route('/get_silence_threshold', methods=['GET'])
def get_silence_threshold():
    try:
        with open('settings.json', 'r') as file:
            settings = json.load(file)
            silence_threshold = settings.get('silence_threshold', 'Not set')
            return jsonify({"silence_threshold": silence_threshold}), 200
    except FileNotFoundError:
        return jsonify({"error": "Settings file not found."}), 404



function getSilenceThreshold() {
        $.ajax({
            url: '/get_silence_threshold',
            type: 'GET',
            success: function(response) {
                $('#currentThreshold').text(response.silence_threshold);
            },
            error: function() {
                $('#currentThreshold').text('Error loading silence threshold');
            }
        });
    }

    // Load the current silence threshold when the page loads
    getSilenceThreshold();
