# base

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/apt) [![Build Status](https://img.shields.io/drone/build/rolehippie/base/master?logo=drone)](https://cloud.drone.io/rolehippie/apt) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/apt)](https://github.com/rolehippie/apt/blob/master/LICENSE) 

Ansible role to install useful basic packages. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

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
  - haveged
```

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
