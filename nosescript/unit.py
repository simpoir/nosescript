import os
import logging

from . import loader
from nose import plugins

LOG = logging.getLogger('nose.' + __name__)


class NoseScriptUnit(plugins.Plugin):
    name = "jscriptunit"

    def wantFile(self, path):
        basename = os.path.basename(path)
        if basename.endswith('.js'):
            return bool(self.conf.testMatch.match(basename))

    def loadTestsFromFile(self, filename):
        return loader.TestRunner(filename, self.conf).load_file(filename)
