#!/usr/bin/python3

from configparser import ConfigParser, NoOptionError
import logging
import requests
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.INFO)

default_config_file = '/etc/googledomains.ini'
default_update_url = 'https://domains.google.com/nic/update'

def get_configs(path):
  parser = ConfigParser()
  parser.read(path)
  return parser

def get_ip_addr(url):
  return requests.get(url).text

def get_session():
  _session = requests.Session()
  logging.debug(_session.headers)
  return _session

def update_dns():
  _config = get_configs(default_config_file)
  _session = get_session()
  _ip_addr = get_ip_addr(_config['DEFAULT'].get('ipsource'))
  url = default_update_url
  for site in _config.sections():
    username = _config[site].get('username')
    if not username:
      raise NoOptionError('No username found for site {} in config {}'.format(
        site, default_config_file))
    password = _config[site].get('password')
    if not password:
      raise NoOptionError('No password found for site {} in config {}'.format(
        site, default_config_file))
    
    data = {
      'hostname': site,
      'myip': _ip_addr
    }

    response = _session.post(url, data=data, 
      auth=HTTPBasicAuth(username, password), verify=True)
    logging.info("{}: HTTP Response {}: {}".format(
      site, response.status_code, response.text))

if __name__=="__main__":
  update_dns()
