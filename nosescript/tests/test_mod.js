QUnit.module("Bogus unit test");

QUnit.test("Fake success", function(assert) {
    assert.equal(2, 1+1);
});

QUnit.test("exceptional case", function(assert) {
    assert.throws(function() {
        var x = null;
        x.y = 42;
    }, /TypeError/);

    assert.throws(function block() {
        assert.throws(function() {
        });
    }, /AssertionError/);

    assert.throws(function() {
        throw "what you expect";
    }, /what you expect/);

    assert.throws(function() {
        throw {message: "what you expect"};
    }, /what you expect/);

    assert.throws(function() {
        assert.throws(function() {
            throw "not the error you were expecting";
        }, /AssertionError/);
    }, QUnit.AssertionError);

    assert.throws(function() {
        assert.throws(function() {
            throw "not the error you were expecting";
        }, QUnit.AssertionError);
    }, QUnit.AssertionError);
});
