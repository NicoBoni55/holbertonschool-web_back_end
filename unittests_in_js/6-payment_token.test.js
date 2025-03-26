const { expect } = require("chai")
const getPaymentTokenFromAPI = require("./6-payment_token")

describe('test promises',function () {
    it('return data', function (done) {
        getPaymentTokenFromAPI(true)
        .then((res) => {
            expect((res).to.include({data: 'Successful response from the API'}))
            done();
        })
        .catch((err) => done(err))
    })
})
