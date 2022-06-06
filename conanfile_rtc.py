from conans import ConanFile


class GSLConan(ConanFile):
    name = "gsl"
    version = "3.1.0"
    url = "https://github.com/Esri/gsl"
    license = "https://github.com/Esri/gsl/blob/master/LICENSE"
    description = "Guidelines Support Library"

    # RTC specific triple
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/gsl/"

        # headers
        self.copy("*.h", src=base + "include/gsl", dst=relative + "include/gsl")

        # no libraries; header-only
