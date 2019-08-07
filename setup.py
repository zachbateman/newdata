import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='newdata',
    version='0.1.0',
    packages=['newdata'],
    license='MIT',
    author='Zach Bateman',
    description='Synthetic data creation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zachbateman/newdata.git',
    download_url='https://github.com/zachbateman/newdata/archive/v_0.1.0.tar.gz',
    keywords=['DATA', 'SYNTHETIC', 'MACHINE LEARNING', 'TRAINING', 'TESTING'],
    install_requires=[],
    classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ]
)