const express = require('express');

const app = express();

app.use(express.json());


app.get("/", (req, resp) => {
    resp.send('Welcome to the payment system')
})

app.get('/cart/:id([0-9]+)', (req, res) => {
    res.end(`Payment methods for cart ${req.params.id}`);
  });

app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      })
  });

app.post('/login', (req, res) => {
    const username = req.body.userName;
    res.send(`Welcome ${username}`)
})

app.listen(7865, () => {
    console.log('API available on localhost port 7865');
})
