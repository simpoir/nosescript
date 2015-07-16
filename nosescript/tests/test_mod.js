QUnit.module("Bogus unit test");

QUnit.test("Fake success", function(assert) {
    barrr();
    assert.equal(2, 1+1);
});

function barrr() {
    throw new Error('oh noes');
}


function Moo(message) {
    this.message = message;
}

QUnit.test("exceptional case", function(assert) {
    assert.throws(function() {
        var x = null;
        x.y = 42;
    }, /TypeError/)
});
