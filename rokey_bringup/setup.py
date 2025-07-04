from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rokey_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # 필수 패키지 인덱스 등록
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # 패키지 설치
        ('share/' + package_name, ['package.xml']),
        
        # launch 파일 설치
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*')),
        
        # rviz 설정 파일 설치
        (os.path.join('share', package_name, 'rviz'),
            glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rokey',
    maintainer_email='llaayy.kr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
