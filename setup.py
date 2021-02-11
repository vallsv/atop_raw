from setuptools import setup


packages = ["atop_raw"]

install_requires = ["pycstruct"]

package_data = {"atop_raw.headers": ["*.h"]}

setup(
    name="atop_raw",
    version="1",
    packages=packages,
    package_data=package_data,
    license="MIT",
    description="Reader of raw files from atop",
    install_requires=install_requires,
)
