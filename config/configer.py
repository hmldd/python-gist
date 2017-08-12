# coding:utf-8
import yaml
import os


def get(key):
    config_path = os.path.dirname(os.path.realpath(__file__))
    file_path = config_path + '/config.yaml'
    stream = file(file_path, 'r')
    config = yaml.load(stream)

    # Load local config
    if config['env'] == 'dev':
        dev_file_path = config_path + '/config-local.yaml'
        stream_local = file(dev_file_path, 'r')
        config_local = yaml.load(stream_local)
        config.update(config_local)

    return config[key]
