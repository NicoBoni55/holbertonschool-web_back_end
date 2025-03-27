const request = require('request');
const chai = require('chai')

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
