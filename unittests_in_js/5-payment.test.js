const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('Hooks', function () {
    let consoleSpy;
    beforeEach(function () {
        consoleSpy = sinon.spy(console, "log")
    })

    afterEach(function () {
        consoleSpy.restore()
    })
    it('sendPaymentRequestToAPI with 100, and 20', () => {
        sendPaymentRequestToApi(100, 20)

        expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
        expect(consoleSpy.calledOnce).to.be.true;

    })

    it('sendPaymentRequestToAPI with 10, and 10', () => {
        sendPaymentRequestToApi(10, 10)

        expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
        expect(consoleSpy.calledOnce).to.be.true;

    })
})
