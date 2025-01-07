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
