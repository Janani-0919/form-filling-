<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voice-Assisted Form</title>
    <style>
        /* General Body Styles */
        body {
            font-family: 'Verdana', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #ff7e5f, #feb47b); /* Gradient Background */
        }

        /* Form Container Styles */
        .form-container {
            background-color: #ffffff; /* White Form Background */
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            width: 90%;
        }

        h1 {
            text-align: center;
            color: #4a4a4a; /* Neutral Heading Color */
            margin-bottom: 20px;
            font-family: 'Georgia', serif;
            font-size: 28px;
        }

        label {
            font-weight: bold;
            color: #333;
            margin-top: 15px;
            display: block;
            font-size: 16px;
        }

        input, textarea, select {
            margin-top: 8px;
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-sizing: border-box;
            background-color: #f9f9f9; /* Light Input Background */
            color: #333;
        }

        input:focus, textarea:focus, select:focus {
            border-color: #ff7e5f;
            outline: none;
            box-shadow: 0 0 10px rgba(255, 126, 95, 0.3);
        }

        button {
            margin-top: 15px;
            padding: 12px;
            width: 100%;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            color: white;
            background-color: #ff7e5f; /* Button Background Color */
            transition: transform 0.2s ease, background-color 0.3s ease;
        }

        button:hover {
            background-color: #e76850;
            transform: scale(1.05); /* Button Hover Animation */
        }

        .voice-button {
            background-color: #48c78e; /* Green Voice Button */
            margin-top: 10px;
            font-size: 16px;
        }

        .voice-button:hover {
            background-color: #3aa572;
            transform: scale(1.05); /* Voice Button Hover Animation */
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Voice-Assisted Form</h1>
        <form id="voiceForm">
            <label for="your-name">Your Name</label>
            <input type="text" id="your-name" name="your-name" placeholder="Enter your name" required>
            <button type="button" class="voice-button" onclick="startVoiceInput('your-name')">🎤 Speak</button>

            <label for="father-name">Father's Name</label>
            <input type="text" id="father-name" name="father-name" placeholder="Enter father's name" required>
            <button type="button" class="voice-button" onclick="startVoiceInput('father-name')">🎤 Speak</button>

            <label for="mother-name">Mother's Name</label>
            <input type="text" id="mother-name" name="mother-name" placeholder="Enter mother's name" required>
            <button type="button" class="voice-button" onclick="startVoiceInput('mother-name')">🎤 Speak</button>

            <label for="address">Address</label>
            <textarea id="address" name="address" placeholder="Enter your address" rows="4" required></textarea>
            <button type="button" class="voice-button" onclick="startVoiceInput('address')">🎤 Speak</button>

            <label for="city">City</label>
            <input type="text" id="city" name="city" placeholder="Enter your city" required>
            <button type="button" class="voice-button" onclick="startVoiceInput('city')">🎤 Speak</button>

            <label for="country">Country</label>
            <select id="country" name="country" required>
                <option value="">Select your country</option>
                <option value="India">India</option>
                <option value="United States">United States</option>
                <option value="United Kingdom">United Kingdom</option>
                <option value="Australia">Australia</option>
                <option value="Canada">Canada</option>
            </select>
            <button type="button" class="voice-button" onclick="startVoiceInput('country')">🎤 Speak</button>

            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-US';
        recognition.interimResults = false;

        function startVoiceInput(fieldId) {
            const field = document.getElementById(fieldId);

            recognition.start();
            recognition.onresult = (event) => {
                const spokenText = event.results[0][0].transcript;

                if (field.tagName.toLowerCase() === "select") {
                    const options = field.options;
                    for (let i = 0; i < options.length; i++) {
                        if (options[i].text.toLowerCase() === spokenText.toLowerCase()) {
                            field.value = options[i].value;
                            break;
                        }
                    }
                } else {
                    field.value = spokenText;
                }
                recognition.stop();
            };

            recognition.onerror = (event) => {
                alert("Speech recognition error: " + event.error);
                recognition.stop();
            };
        }
    </script>
</body>
</html>
