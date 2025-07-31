import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function createHash() {
    client.hSet('HolbertonSchools', 'Portland', '50')
        .then(() => console.log('Reply: 1'))
        .catch(err => console.log(err));
    
    client.hSet('HolbertonSchools', 'Seattle', '80')
        .then(() => console.log('Reply: 1'))
        .catch(err => console.log(err));

    client.hSet('HolbertonSchools', 'New York', '20')
        .then(() => console.log('Reply: 1'))
        .catch(err => console.log(err));

    client.hSet('HolbertonSchools', 'Bogota', '20')
        .then(() => console.log('Reply: 1'))
        .catch(err => console.log(err));

    client.hSet('HolbertonSchools', 'Cali', '40')
        .then(() => console.log('Reply: 1'))
        .catch(err => console.log(err));

    client.hSet('HolbertonSchools', 'Paris', '2')
        .then(() => console.log('Reply: 1'))
        .catch(err => console.log(err));
}

function displayHash() {
    client.hGetAll('HolbertonSchools')
        .then((result) => {
            console.log(JSON.stringify(result, null, 2));
        })
        .catch((err) => {
            console.log(err);
        });
}

(async () => {
    await client.connect();

    createHash();

    setTimeout(() => {
        displayHash();
    }, 500);
})();