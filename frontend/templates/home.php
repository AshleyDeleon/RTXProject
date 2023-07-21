<?php
// Get the form data
$email = $_POST['textbox1'];
$password = $_POST['textbox2'];

// Validate and sanitize the data if needed

// Connect to the database
$conn = new mysqli("localhost", "username", "password", "database_name");

// Check the connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Insert the data into the database
$sql = "INSERT INTO users (email, password) VALUES ('$email', '$password')";
if ($conn->query($sql) === TRUE) {
  echo "Data stored successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close the database connection
$conn->close();
?>
