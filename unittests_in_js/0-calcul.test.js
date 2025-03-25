const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Calculate Numbers', function(){
    it('return 4, 1 + 3', function(){
        assert.strictEqual(calculateNumber(1, 3), 4)
    })
    it('return 5, 1 + 3.7', function(){
        assert.strictEqual(calculateNumber(1, 3.7), 5)
    })
    it('return 5, 1.2 + 3.7', function(){
        assert.strictEqual(calculateNumber(1.2, 3.7), 5)
    })
    it('return 6, 1.5 + 3.7', function(){
        assert.strictEqual(calculateNumber(1.5, 3.7), 6)
    })
    it('return -4, -1 + -3', function(){
        assert.strictEqual(calculateNumber(-1, -3), -4)
    })
    it('return 0, 0 + 0', function(){
        assert.strictEqual(calculateNumber(0, 0), 0)
    })
});

describe('check args', function(){
    it('check arg', function(){
        assert.strictEqual(isNaN(calculateNumber(1)), true);
        assert.strictEqual(isNaN(calculateNumber()), true);
    })
});
