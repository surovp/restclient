from distutils.core import setup
REQUIRES = [
    'structlog',
    'requests',
    'allure-pytest',
    'curlify'
]

setup(
    name='restclient',
    version='0.0.2',
    packages=['restclient'],
    url='https://github.com/surovp/restclient.git',
    license='MIT',
    author='Pavel Surov',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with log and send request'
)
