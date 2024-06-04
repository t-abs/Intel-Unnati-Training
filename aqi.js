function predictAQI() {
    // Retrieve input values
    const pm25 = parseFloat(document.getElementById('pm25').value);
    const ozone = parseFloat(document.getElementById('ozone').value);
    const co = parseFloat(document.getElementById('co').value);
    const no2 = parseFloat(document.getElementById('no2').value);

    // Basic AQI calculation logic (for demonstration)
    const aqi = (pm25 * 0.4) + (ozone * 0.3) + (co * 0.2) + (no2 * 0.1);

    // Determine AQI category
    let category;
    if (aqi <= 50) {
        category = 'Good';
    } else if (aqi <= 100) {
        category = 'Moderate';
    } else if (aqi <= 150) {
        category = 'Unhealthy for Sensitive Groups';
    } else if (aqi <= 200) {
        category = 'Unhealthy';
    } else if (aqi <= 300) {
        category = 'Very Unhealthy';
    } else {
        category = 'Hazardous';
    }

    // Display the result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `Predicted AQI: ${aqi.toFixed(2)}<br>Category: ${category}`;
}
