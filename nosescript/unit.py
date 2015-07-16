import os
import logging

from . import loader
from nose import plugins

LOG = logging.getLogger('nose.' + __name__)


class NoseScriptUnit(plugins.Plugin):
    name = "jscriptunit"

    def options(self, parser, env=os.environ):
        super(NoseScriptUnit, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NoseScriptUnit, self).configure(options, conf)
        LOG.info('Configuring JavaScript Unit testing')
        if not self.enabled:
            return

    def finalize(self, result):
        LOG.info('JavaScript Unit testing done')

    def wantFile(self, path):
        basename = os.path.basename(path)
        return (basename.endswith('.js')
                and self.conf.testMatch.match(basename))

    def loadTestsFromFile(self, filename):
        return loader.TestRunner(filename, self.conf).load_file(filename)
