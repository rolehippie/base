# base

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/base/status.svg)](https://cloud.drone.io/rolehippie/base)

Ansible role to install basics

## Table of content

* [Default Variables](#default-variables)
  * [base_ubuntu_additional](#base_ubuntu_additional)
  * [base_ubuntu_packages](#base_ubuntu_packages)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### base_ubuntu_additional

Additionally install on Ubuntu

#### Default value

```YAML
base_ubuntu_additional: []
```

### base_ubuntu_packages

List of packages to install on Ubuntu

#### Default value

```YAML
base_ubuntu_packages:
  - apt-transport-https
  - software-properties-common
  - tree
  - htop
  - iotop
  - sysstat
  - ipvsadm
  - update-notifier-common
  - socat
  - jq
  - curl
  - apt-dater-host
  - net-tools
  - traceroute
  - acl
```

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
