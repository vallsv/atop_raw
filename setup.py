from setuptools import setup


packages = ["atop_raw", "atop_raw.headers"]

install_requires = ["numpy"]

extras_require = {"pycstruct": ["pycstruct >= 0.9"]}

package_data = {"atop_raw.headers": ["*.h"]}

setup(
    name="atop_raw",
    version="2",
    packages=packages,
    extras_require=extras_require,
    package_data=package_data,
    license="MIT",
    description="Reader of raw files from atop",
    install_requires=install_requires,
)
