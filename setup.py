from setuptools import find_packages, setup
import sessionista

DESCRIPTION = 'Just another way to think about server side sessions.'

setup(
    name='sessionista',
    packages=find_packages(),
    include_package_data=True,
    version=sessionista.__version__,
    description=DESCRIPTION,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django'
    ],
    author='Pablo Rivera',
    author_email='privera@celerity.com',
    url='https://github.com/pabloriveracelerity/sessionista',
    license='MIT',
    zip_safe=False,
)