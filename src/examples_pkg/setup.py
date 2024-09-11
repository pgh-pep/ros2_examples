from setuptools import find_packages, setup

package_name = 'examples_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='varun',
    maintainer_email='varunpat789@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={          # Make sure to add new nodes here
        'console_scripts': [        # 'node_executable_name = pkg_name.file_name:main'
            'base_python_node = examples_pkg.base_python_node:main',
            'example_publisher = examples_pkg.example_publisher:main',
            'example_subscriber = examples_pkg.example_subscriber:main',
            'example_server = examples_pkg.example_server:main',
            'example_client = examples_pkg.example_client:main'
        ],
    },
)
