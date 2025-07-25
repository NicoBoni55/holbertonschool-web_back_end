import { createClient} from 'redis';

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

async function displaySchoolValue(schoolName) {
    try {
        const result = await client.get(schoolName);
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