document.getElementById('aqiForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const aqiValue = data.aqi;
        const aqiCategory = getAQICategory(aqiValue);
        document.getElementById('result').innerHTML = `Predicted AQI: ${aqiValue}`;
        document.getElementById('aqiCategory').innerHTML = `Category: ${aqiCategory}`;
        
    
    })
    .catch(error => {
        document.getElementById('result').innerHTML = `Error: ${error}`;
    });
});


function getAQICategory(aqiValue) {
    if (aqiValue >= 0 && aqiValue <= 50) {
        return 'Good';
    } else if (aqiValue >= 51 && aqiValue <= 100) {
        return 'Satisfactory';
    } else if (aqiValue >= 101 && aqiValue <= 150) {
        return 'Moderately polluted';
    } else if (aqiValue >= 151 && aqiValue <= 200) {
        return 'Poor';
    } else if (aqiValue >= 201 && aqiValue <= 300) {
        return 'Very Poor';
    } else if (aqiValue >= 301 && aqiValue <= 500) {
        return 'Severe';
    } else {
        return 'Unknown';
    }
}

