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
