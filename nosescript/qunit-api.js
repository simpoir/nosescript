// Micro implementation of QUnit API.
QUnit.module = function module(name, hooks) {
    QUnit._module(name, hooks);
};

QUnit.test = function(name, test) {
    QUnit._test(name, function() {
        try {
            test(QUnit.assert);
        } catch (e) {
            return {
                name: e.name,
                message: e.message,
                stack: e.stack
            };
        }
    });
};

QUnit.assert = {
};
