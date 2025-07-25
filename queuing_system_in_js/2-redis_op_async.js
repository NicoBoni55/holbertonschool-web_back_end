import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value) {
    try {
        await client.set(schoolName, value);
        console.log('Reply: OK');
    } catch (err) {
        console.log(err);
    }
}

function getCallback(key, callback) {
    client.get(key)
        .then(result => callback(null, result))
        .catch(err => callback(err, null));
}

const getAsync = promisify(getCallback);

async function displaySchoolValue(schoolName) {
    try {
        const result = await getAsync(schoolName);
        console.log(result);
    } catch (err) {
        console.log(err);
    }
}

(async () => {
    await client.connect();
    
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();