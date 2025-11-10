# base

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/base)
[![General Workflow](https://github.com/rolehippie/base/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/base/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/base/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/base/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/base/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/base/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/base)](https://github.com/rolehippie/base/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.base-blue)](https://galaxy.ansible.com/rolehippie/base)

Ansible role to install useful basic packages.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of contents

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [base_debian_additional](#base_debian_additional)
  - [base_debian_packages](#base_debian_packages)
  - [base_ubuntu_additional](#base_ubuntu_additional)
  - [base_ubuntu_packages](#base_ubuntu_packages)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### base_debian_additional

Additionally install on Debian

#### Default value

```YAML
base_debian_additional: '{{ base_ubuntu_additional }}'
```

### base_debian_packages

List of packages to install on Debian

#### Default value

```YAML
base_debian_packages: '{{ base_ubuntu_packages }}'
```

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
  - tmux
```

## Discovered Tags

**_base_**

## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
