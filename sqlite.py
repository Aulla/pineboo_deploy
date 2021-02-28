from pyqtdeploy import Component, ComponentLibrary

class sqliteComponent(Component):

    def get_archive_name(self):
        """ Return the filename of the source archive. """

        return 'sqlite-autoconf-{}.tar.gz'.format(str(self.version).split(".")[0])
    
    def get_archive_urls(self):
        """ Return the list of URLs where the source archive might be
        downloaded from.
        """

        return ['https://www.sqlite.org/2021/']
    
    def install(self):
        """ Install for the target. """

        if not self.install_from_source:
            return

        # Unpack the source.
        self.unpack_archive(self.get_archive())


        self.run('./configure', '--enable-static', '--prefix=' + self.sysroot_dir)
        self.run(self.host_make)
        self.run(self.host_make, 'install')
    
    @property
    def provides(self):
        """ The dict of parts provided by the component. """

        return {'sqlitelib': ComponentLibrary(libs=('win#-lsqlitelib', '!win#-lsqlite'))}




    
    def verify(self):
        """ Verify the component. """

        if not self.install_from_source:
            self._verify_installed_version()
    
    #def _verify_installed_version(self):
    #    current_version = "3330000"
    #    if str(self.version) != current_version:

    #        self.error("Incomplatible version %s < %s" % (current_version, self.version))
