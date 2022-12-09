from setuptools import setup
import os
from glob import glob

package_name = 'prius_sdc_pkg'
config_module = 'prius_sdc_pkg/config'
det_module = 'prius_sdc_pkg/Detection'
det_l_module = 'prius_sdc_pkg/Detection/Lanes'
# data_module ="prius_sdc_pkg/data"

# detection_module ="prius_sdc_pkg/Detection"
# gps_navigation = "prius_sdc_pkg/GPS_Navigation"

# det_l_module ="prius_sdc_pkg/Detection/Lanes"
# detec_l_a_module="prius_sdc_pkg/Detection/Lanes/a_Segmentation"
# detec_l_b_module="prius_sdc_pkg/Detection/Lanes/b_Estimation"
# detec_l_c_module="prius_sdc_pkg/Detection/Lanes/c_Cleaning"
# detec_l_d_module="prius_sdc_pkg/Detection/Lanes/d_LaneInfo_Extraction"

det_s_module ="prius_sdc_pkg/Detection/Signs"
detec_s_a_module="prius_sdc_pkg/Detection/Signs/Classification"

detec_TL_module="prius_sdc_pkg/Detection/TrafficLights"
setup(
    name=package_name,
    version='0.0.0',
packages=[package_name,config_module,det_module, det_l_module],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('lib', package_name), glob('scripts/*')),
        (os.path.join('share', package_name,'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aditya',
    maintainer_email='adinisal12@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'recorder_node = prius_sdc_pkg.video_recorder:main',
            'driver_node = prius_sdc_pkg.driving_node:main',
            'spawner_node = prius_sdc_pkg.sdf_spawner:main',
            'computer_vision_node = prius_sdc_pkg.computer_vision_node:main',
        ],
    },
)
