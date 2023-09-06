// Get the textarea element
const textarea = document.getElementById('inputTextarea');
const sendButton = document.getElementById('sendButton');

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
