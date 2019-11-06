import os
from conans import ConanFile, tools


class TinytomlConan(ConanFile):
    name = "tinytoml"
    version = "0.4"
    description = "A header only C++11 library for parsing TOML"
    topics = ("conan", "tinytoml", "toml", "header-only")
    url = "https://github.com/bincrafters/conan-tinytoml"
    homepage = "https://github.com/mayah/tinytoml"
    license = "BSD-2-Clause"
    no_copy_source = True
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "bd5e330dcddceba26a2794f543071e0ef2a62ea52afb322d23674c36060e0afa"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
