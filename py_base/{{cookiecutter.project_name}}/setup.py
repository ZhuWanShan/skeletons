#from pip.req import parse_requirements
import os
from shutil import copyfile


try:
    from setuptools import setup
    except ImportError:
        from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

config = {
           'description': 'XPoint Deployment cli',
                      'author': 'Spark Zhu',
                                 'url': 'URL to get it at.',
                                            'download_url': 'Where to download it.',
                                                       'author_email': 'szhu@coupang.com',
                                                                  'version': '0.1',
                                                                             'install_requires': required,
                                                                                        'packages': ['xpoint_deploy_cli'],
                                                                                                   'scripts': ['bin/xpoint'],
                                                                                                              'name': 'xpoint_deploy_cli'
                                                                                                                        }

setup(**config)


def main():
    print("#"*50 + "Create Config files" + "#"*50)
        default_setting_dir = '/pang/conf/xpoint/'
            default_setting_file = "setting.yaml"

    if not os.path.exists(default_setting_dir):
            os.makedirs(default_setting_dir)

    current_dir = os.path.dirname(os.path.realpath(__file__))

    copyfile(current_dir + "/resources/setting.yaml", default_setting_dir + "/setting.yaml")
        copyfile(current_dir + "/resources/setting_itg.yaml", default_setting_dir + "/setting_itg.yaml")
            copyfile(current_dir + "/resources/setting_prod.yaml", default_setting_dir + "/setting_prod.yaml")

    print("Setting files are copied to {}".format(default_setting_dir))


if __name__ == '__main__':
    main()
    
