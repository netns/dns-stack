# DNS Stack configuration and scripts

This repository provides a set of configuration files and helper scripts
for setting up DNS services. The intent is to provide a reusable
infrastructure for authoritative and recursive DNS, including
BIND, Unbound, and related tools.

## Usage

- Review and adjust configurations under `etc-unbound`, `etc-bind` and `zones`.
- Place configuration files in the appropriate directories (e.g.,
   `/etc/bind/` for BIND or `/etc/unbound/` for Unbound).
- Use helper scripts under `scripts/` for management tasks.
- Test your DNS server configuration with standard tools:

```bash
named-checkconf
named-checkzone example.com zones/example.com.zone
```

- Start or restart the DNS services.

## Contributing

Contributions are welcome. Please open an issue or pull request.

## License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.
