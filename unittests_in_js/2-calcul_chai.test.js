const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
    it('checks the output', () => {
        chai.expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        chai.expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        chai.expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
