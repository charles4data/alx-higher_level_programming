#!/usr/bin/node

// Imports the Request Module
const request = require('request'); 

// Checks number of arguments
if (process.argv.length < 3) {
  console.error("Error: Please provide the API URL as an argument.");
  process.exit(1);
}

// Assigns URL to variable
const apiUrl = process.argv[2];

// Computes the number of tasks completed by user id
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  try {
    const todos = JSON.parse(body);

    const completedTasksByUser = {};

    // Iterate through each task and count completed tasks per user
    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    }

    // Print user IDs with completed tasks
    for (const userId in completedTasksByUser) {
      console.log(`User ID ${userId}: ${completedTasksByUser[userId]} completed tasks`);
    }

  } catch (jsonError) {
    console.error('Error parsing JSON:', jsonError);
  }
});
