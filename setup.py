import sys
from setuptools import setup

long_description = open('README.md').read()

reqs = []
if [sys.version_info[0], sys.version_info[1]] < [2, 7]:
    reqs.append("simplejson>=2.0.9")

setup(
    name='ak-django-datadog',
    version='0.1.0.5',
    packages=[
        'datadog',
        'datadog.middleware'
    ],
    include_package_data=True,
    license='BSD',
    description=(
        'Simple Django middleware for submitting timings and exceptions to'
        ' Datadog.'),
    long_description=long_description,
    author='Conor Branagan',
    author_email='conor.branagan@gmail.com',
    install_requires=reqs.extend([
        'dogapi==1.2.1'
    ])
)
