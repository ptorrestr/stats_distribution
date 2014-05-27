from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='stats_distribution',
    version='0.0.1',
    description='Print out the distribution for a text corpus data',
    long_description = readme(),
    classifiers=[
      'Programming Language :: Python :: 2.7',
    ],
    url='http://github.com/ptorrest/stats_distribution',
    author='Pablo Torres',
    author_email='pablo.torres@deri.org',
    license='GNU',
    packages=['stats_distribution', 'stats_distribution.tests'],
    install_requires=[],
    entry_points = {
        'console_scripts':[
            'count_mapper = stats_distribution.mapreduce:mapper',
            'count_reducer = stats_distribution.mapreduce:reducer',
            'count_cat = stats_distribution.reader:cat',
        ]
    },
    scripts = ['bash/count_local'],
    test_suite='stats_distribution.tests',
    zip_safe = False
)
