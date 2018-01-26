from distutils.core import setup
import versioneer

setup(
    name='epigraf',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Julien Machiels',
    author_email='iamtimscampi@gmail.com',
    packages=['epigraf', 'epigraf.test'],
    license='LICENSE.txt',
    description='Next-generation file management for data hoarders.',
    long_description=open('README.txt').read(),
    install_requires=[
        'PyQt5',],
)

