let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let data = JSON.stringify({ "textToAnalyze": textToAnalyze });

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            
            let response = JSON.parse(xhttp.responseText);

            document.getElementById("system_response").innerHTML = response.response || response.console.error;
        }
    };

    xhttp.open("GET", "/sentimentAnalyzer", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(data);
}
