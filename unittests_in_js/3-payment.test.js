const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('Spies', function() {
    it('as the same', () => {
        const calculateNumberSpy = sinon.spy(Utils, "calculateNumber");

        const consoleSpy = sinon.spy(console, "log");

        sendPaymentRequestToApi(100, 20)

        expect(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;

        calculateNumberSpy.restore()
        consoleSpy.restore()
    })
})
