let jsonData;
let id;
let message_content;
let transposedData;
document.addEventListener('DOMContentLoaded', async function () {
    // Get the data-id attribute from the body element
    const section = document.querySelector('section[data-id]');
    id = section.getAttribute('data-id');

    // Make an AJAX request to fetch the data from the API using the retrieved id
    await fetch(`/api/data/${id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            jsonData = data;
            get_xyz(jsonData);
            createBarChart(transposedData[0], transposedData[1]);
             // Call the function to create a new bar chart with a new canvas
            // Here, you can process the fetched data as needed, such as populating the table
            // Example: Populate a table with the fetched data
            const tableBody = document.getElementById("table");
      
            jsonData.forEach(item => {
                const row = document.createElement('tr');
                
                for (const key in item) {
                    if (item.hasOwnProperty(key)) {
                        const cell = document.createElement('td');
                        cell.textContent = item[key];
                        row.appendChild(cell);
                    }
                }
      
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
});


// Function to send a message to the chatbot
function sendMessageToChatbot(messageInput) {
	// Define the URL of your Flask server's /chatbot route
	const url = '/chatbot';

	// Get the message from the input field
	const message =
		messageInput +
		"(return a full JSON only don't return any text): " +
		JSON.stringify(jsonData);

	// Create a data object with the message
	const data = { message };
	console.log(data);

	// Configure the fetch request
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	})
		.then((response) => response.json())
		.then((responseJson) => {
			// Handle the chatbot's response here (responseJson)
			

			message_content = responseJson['answer']['choices'][0]['message']['content'];
            console.log(message_content);
     
			// You can perform additional actions here with the chatbot's response
			
		})
		.catch((error) => {
			console.error('Error:', error);
		});
}


function get_xyz(data){
// Initialize arrays for x, y, and z values
var xValues = [];
var yValues = [];

// Loop through the JSON data to extract values and transpose them
for (var i = 0; i < jsonData.length; i++) {
  xValues.push(data[i]["departure_place"]);
  yValues.push(data[i]["period"]);
}

// Transpose the arrays into an array of arrays
transposedData = [xValues, yValues];

console.log(transposedData);
}


function generateRandomColors(length) {
    const uniqueColors = new Set(); // Use a Set to ensure uniqueness
  
    // Function to generate a random color in hexadecimal format
    function getRandomColor() {
      const letters = "0123456789ABCDEF";
      let color = "#";
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    }
  
    // Generate unique random colors
    while (uniqueColors.size < length) {
      uniqueColors.add(getRandomColor());
    }
  
    // Convert Set to an array
    const colorsArray = Array.from(uniqueColors);
    return colorsArray;
  }
  


  




function createBarChart(xValues, yValues) {
    // Create a new canvas element
    var canvas = document.createElement('canvas');

    canvas.width = 400;
    canvas.height = 250;
    canvas.style.margin = 'auto'; // Center the canvas horizontally
    canvas.style.display = 'block'; // Make the canvas a block element
  
    // Style the canvas (adjust these styles as needed)

    // Generate a unique ID for the canvas
    var canvasId = 'canvas' + new Date().getTime();
    canvas.id = canvasId;
 
    // Append the canvas to a container in your HTML (you may need to adjust this part)
    document.getElementById('chartContainer').appendChild(canvas);
  
    var ctx = canvas.getContext('2d');
    
    
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: xValues,
        datasets: [{
          backgroundColor:   // Example usage to generate 5 unique random colors
          randomColors = generateRandomColors(xValues.length),
          data: yValues,
        }]
      },
      options: {
        title: {
          display: true,
          text: "How long have the ship stayed in each country over the past year"
        },
  
      }
    });
  }
  

  
 
