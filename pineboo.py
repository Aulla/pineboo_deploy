import os
import shutil
from pyqtdeploy import Component, PythonPackage


class pinebooComponent(Component):

    preinstalls = ['Python']

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

        if not self.install_from_source:
            self.error("need install from source")
            return

        else:

            self.unpack_archive(self.get_archive())
            self.copy_dir('.', os.path.join(self.target_include_dir))

    @property
    def provides(self):
        """ The dict of parts provided by the component. """

        #pyqt_platform = self.target_platform_name

        # if pyqt_platform == 'android':
        #    pyqt_platform = 'linux'
        # elif pyqt_platform in ('ios', 'macos'):
        #    pyqt_platform = 'darwin'
        # elif pyqt_platform == 'win':
        #    pyqt_platform = 'win32'

        parts = {
            'pineboo': PythonPackage(
                deps=('Python:io', 'Python:logging', 'Python:os', 'Python:re',
                      'Python:traceback', 'Python:xml.etree.ElementTree'),
            ),

        }

        return parts

    def verify(self):
        """ Verify the component. """

        if not self.install_from_source:
            self._verify_installed_version()

    def _verify_installed_version(self):

        from pineboolib import application
        if str(self.version) > application.PINEBOO_VER:

            self.error("Incomplatible version %s < %s" %
                       (application.PINEBOO_VER, self.version))
