from setuptools import setup
import os
from glob import glob 


package_name = 'self_driving_car_pkg'

# det_l_module ="self_driving_car_pkg/Detection/Lanes"
# det_s_module ="self_driving_car_pkg/Detection/Signs"
# config_module = "self_driving_car_pkg/config" 
# data_module ="self_driving_car_pkg/data"
# control_module ="self_driving_car_pkg/Control"
# detec_l_a_module="self_driving_car_pkg/Detection/Lanes/a_Segmentation"
# detec_l_b_module="self_driving_car_pkg/Detection/Lanes/b_Estimation"
# detec_l_c_module="self_driving_car_pkg/Detection/Lanes/c_Cleaning"
# detec_l_d_module="self_driving_car_pkg/Detection/Lanes/d_LaneInfo_Extraction"

# detec_s_a_module="self_driving_car_pkg/Detection/Signs/a_Localization"
# detec_s_b_module="self_driving_car_pkg/Detection/Signs/b_Classification"
# detec_s_c_module="self_driving_car_pkg/Detection/Signs/c_Tracking"
    # packages=[package_name,detec_s_a_module,detec_s_b_module,detec_s_c_module,detec_l_d_module,detec_l_c_module,detec_l_b_module,config_module,det_l_module,det_s_module,data_module,control_module,detec_l_a_module],


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('share', package_name,'scripts'), glob('scripts/*')),


            ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'spawner_node = self_driving_car_pkg.sdf_spawner:main',
        'computer_vision_node = self_driving_car_pkg.computer_vision_node:main',
        'video_recording_node = self_driving_car_pkg.video_save:main',
        ],
    },
)
