import os, shutil
from pyqtdeploy import Component

class pineboolib(Component):
    

    def get_archive_name(self):
        """ Return the filename of the source archive. """

        return 'pineboo-{}.tar.gz'.format(self.version)
    
    def get_archive_urls(self):
        """ Return the list of URLs where the source archive might be
        downloaded from.
        """

        return self.get_pypi_urls('pineboo')

    def install(self):
        """ Install for the target. """

        self.unpack_archive(self.get_archive())
    
    def verify(self):
        """ Verify the component. """

        if not self.install_from_source:
            self._verify_installed_version()
        

    def _verify_installed_version(self):

        from pineboolib import application
        if str(self.version) > application.PINEBOO_VER:

            self.error("Incomplatible version %s < %s" % (application.PINEBOO_VER, self.version))