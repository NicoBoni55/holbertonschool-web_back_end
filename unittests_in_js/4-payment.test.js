const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('Spies', function() {
    it('allways return 10', () => {
        const calculateNumberStub = sinon.stub(Utils, "calculateNumber");
        calculateNumberStub.returns(10)
        const consoleSpy = sinon.spy(console, "log");

        sendPaymentRequestToApi(100, 20)

        expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

        calculateNumberStub.restore()
        consoleSpy.restore()
    })
})
