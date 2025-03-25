const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    it('checks the output', () => {
      it('check sum', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      })
      it('check subtract', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      })
      it('check divide', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
      })
      it('check error', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      })
      it('check error', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 0), 1);
      })
    });
});