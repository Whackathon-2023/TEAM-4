// Get the textarea element
const textarea = document.getElementById('inputTextarea');
const sendButton = document.getElementById('sendButton');
const answerTextarea = document.getElementById('answerTextarea');

// Function to adjust the number of rows based on content
function adjustTextareaRows() {
	const minimumRows = 3; // Set a minimum of 3 rows
	const lineHeight = parseInt(getComputedStyle(textarea).lineHeight);

	const previousRows = textarea.rows;
	textarea.rows = minimumRows; // Reset rows to the minimum

	const currentRows = Math.min(
		Math.floor(textarea.scrollHeight / lineHeight),
		10
	);
	textarea.rows = Math.max(currentRows, minimumRows); // Set rows to the maximum of currentRows and minimumRows

	// If rows have changed, you can perform any necessary actions here
	if (textarea.rows !== previousRows) {
		// Rows have changed, you can perform actions here
	}
}

// Attach an event listener for input
textarea.addEventListener('input', adjustTextareaRows);

// Initially adjust rows based on placeholder text
adjustTextareaRows();

// Function to check if there is text in the textarea and change the button color
function checkTextareaContent() {
	if (textarea.value.trim() !== '') {
		sendButton.classList.add('send-btn-allowed'); // Add the blue-button class
	} else {
		sendButton.classList.remove('send-btn-allowed'); // Remove the blue-button class
	}
}

// Attach an event listener for input in the textarea
textarea.addEventListener('input', checkTextareaContent);

// Initially check textarea content on page load
checkTextareaContent();

function senddata() {
	const msg =
		"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.";
	if (textarea.value.trim() !== '') {
		answerTextarea.innerText = msg;
	}
}
