const request = require('request');
const chai = require('chai');
const { json } = require('express');

describe('test api', () => {
    it('status and message', (done) => {
        const options = {
            url: "http://localhost:7865",
            method: "GET",
        };

        request(options, (error, response, body) => {
            chai.expect(response.statusCode).to.equal(200);
            chai.expect(body).to.equal('Welcome to the payment system');
            done();
        })
    })
})
describe('test route cart/', () => {
    it('status and message', (done) => {
        const options = {
            url: "http://localhost:7865/cart/12",
            method: "GET",
        };

        request(options, (error, response, body) => {
            chai.expect(response.statusCode).to.equal(200);
            chai.expect(body).to.equal('Payment methods for cart 12');
            done();
        })
    })
    it('status and message - with letters', (done) => {
        const options = {
            url: "http://localhost:7865/cart/a12",
            method: "GET",
        };

        request(options, (error, response, body) => {
            chai.expect(response.statusCode).to.equal(404);
            done();
        })
    })
})
describe('test available_payments and login', () => {
    it('status and message', (done) => {
        const options = {
            url: "http://localhost:7865/available_payments",
            method: "GET",
        };

        request(options, (error, response, body) => {
            chai.expect(response.statusCode).to.equal(200);
            chai.expect(body).to.equal( '{"payment_methods":{"credit_cards":true,"paypal":false}}');
            done();
        })
    })
    it('login', (done) => {
        const options = {
            url: "http://localhost:7865/login",
            method: "POST",
            json: {
                userName: 'Carlos'
            }
        };

        request(options, (error, response, body) => {
            chai.expect(response.statusCode).to.equal(200);
            chai.expect(body).to.equal('Welcome Carlos')
            done();
        })
    })
    it('login with no username', (done) => {
        const options = {
            url: "http://localhost:7865/login",
            method: "POST",
            json: {}
        };

        request(options, (error, response, body) => {
            chai.expect(response.statusCode).to.equal(200);
            chai.expect(body).to.equal('Welcome undefined')
            done();
        })
    })
})
