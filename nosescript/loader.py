import os
import logging
import spidermonkey

from .bridge import qunit

LOG = logging.getLogger('nose.' + __name__)
_runtime = spidermonkey.Runtime()


class TestRunner(object):
    def __init__(self, path, conf):
        super(TestRunner, self).__init__()
        self._ctx = _runtime.new_context()
        self._qunit = qunit.QUnit(self._ctx)

    def load_file(self, path):
        LOG.info('Loading tests from %s', path)
        mod_name = os.path.basename(path).rpartition(os.path.extsep)[0]
        self._qunit.module(mod_name)
        with open(path) as f:
            script = f.read()
            self._qunit.source = script
            self._ctx.execute(script, filename=path)
        for test in self._qunit.tests:
            yield test
        if not len(self._qunit.tests):
            yield False
