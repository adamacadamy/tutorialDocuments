const fetch = require('node-fetch');
const fs = require('fs');

// Test the /upload/image endpoint
async function testUpload() {
    const url = 'http://localhost:5000/upload/image';
    const data = new FormData();
    data.append('image', fs.createReadStream('./images/image.jpg')); // Replace with actual path
    data.append('name', 'John Doe');
    data.append('email', 'john@example.com');

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: data
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const json = await response.json();
        console.log('Success! Upload Response:');
        console.log(json);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Test the /users/create endpoint
async function testCreateUser() {
    const url = 'http://localhost:5000/users/create';
    const data = new FormData();
    data.append('name', 'Jane Doe');
    data.append('email', 'jane@example.com');

    try {
        const response = await fetch(url, {
            method: 'POST',
            body: data
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const json = await response.json();
        console.log('Success! Create User Response:');
        console.log(json);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Run both tests
 
console.log('Testing Upload Endpoint...');
await testUpload();
console.log('\nTesting Create User Endpoint...');
await testCreateUser();
 