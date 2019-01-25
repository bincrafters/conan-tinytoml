#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class TinytomlConan(ConanFile):
    name = "tinytoml"
    version = "0.4"
    description = "A header only C++11 library for parsing TOML"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "toml")
    url = "https://github.com/bincrafters/conan-tinytoml"
    homepage = "https://github.com/mayah/tinytoml"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD-2-Clause"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/mayah/tinytoml"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="bd5e330dcddceba26a2794f543071e0ef2a62ea52afb322d23674c36060e0afa")
        extracted_dir = self.name + "-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)


    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)


    def package_id(self):
        self.info.header_only()
