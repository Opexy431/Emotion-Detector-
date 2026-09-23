let RunSentimentAnalysis = () => {
    const textElement = document.getElementById("textToAnalyze");
    const responseContainer = document.getElementById("system_response");
    const textToAnalyze = textElement.value.trim();

    if (!textToAnalyze) {
        responseContainer.className = "p-3 border rounded text-danger bg-danger-subtle";
        responseContainer.innerHTML = "<strong>Invalid text! Please try again!</strong>";
        return;
    }

    responseContainer.className = "p-3 border rounded bg-light text-muted";
    responseContainer.innerHTML = '<div class="spinner-border spinner-border-sm text-primary me-2" role="status"></div> Analyzing emotions...';

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            if (this.status === 200) {
                const responseText = this.responseText;
                if (responseText.includes("Invalid text")) {
                    responseContainer.className = "p-3 border rounded text-danger bg-danger-subtle";
                    responseContainer.innerHTML = `<strong>${responseText}</strong>`;
                } else {
                    responseContainer.className = "p-3 border rounded text-dark bg-white shadow-sm";
                    responseContainer.innerHTML = `
                        <div class="alert alert-success border-0 mb-3">
                            <i class="fa-solid fa-circle-check me-2"></i><strong>Analysis Complete</strong>
                        </div>
                        <p class="mb-0 fs-6">${responseText}</p>
                    `;
                }
            } else {
                responseContainer.className = "p-3 border rounded text-danger bg-danger-subtle";
                responseContainer.innerHTML = "<strong>Invalid text! Please try again!</strong>";
            }
        }
    };

    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
