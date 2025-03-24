const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Calculate Numbers', function(){
    it('return 4, 1 + 3', function(){
        let result = calculateNumber(1, 3)
        assert.strictEqual(result, 4)
    })
    it('return 5, 1 + 3.7', function(){
        let result = calculateNumber(1, 3.7)
        assert.strictEqual(result, 5)
    })
    it('return 5, 1.2 + 3.7', function(){
        let result = calculateNumber(1.2, 3.7)
        assert.strictEqual(result, 5)
    })
    it('return 6, 1.5 + 3.7', function(){
        let result = calculateNumber(1.5, 3.7)
        assert.strictEqual(result, 6)
    })
});
