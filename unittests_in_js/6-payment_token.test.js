const { expect } = require("chai")
const getPaymentTokenFromAPI = require("./6-payment_token")

describe('test promises', function () {
    it('return data', function (done) {
        getPaymentTokenFromAPI(true).then((result) => {
            expect(result).to.deep.equal({ data: 'Successful response from the API' })
            done();
        }).catch(done);
    })
})
