# {{cookiecutter.package_name}}

[![License {{cookiecutter.license}}](https://img.shields.io/pypi/l/{{cookiecutter.package_name}}.svg?color=green)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.package_name}}.svg?color=green)](https://pypi.org/project/{{cookiecutter.package_name}})
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.package_name}}.svg?color=green)](https://python.org)
[![tests](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}/workflows/tests/badge.svg)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}/actions)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}})


{{cookiecutter.short_description}}

----------------------------------

This [caped] package was generated with [Cookiecutter] using [@caped]'s [cookiecutter-template] template.



## Installation

You can install `{{cookiecutter.package_name}}` via [pip]:

    pip install {{cookiecutter.package_name}}


{% if cookiecutter.github_repository_url != 'provide later' %}
To install latest development version :

    pip install git+https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}.git
{% endif %}

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [{{cookiecutter.license}}] license,
"{{cookiecutter.package_name}}" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.


[pip]: https://pypi.org/project/pip/
[caped]: https://github.com/Kapoorlabs-CAPED
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@caped]: https://github.com/Kapoorlabs-CAPED
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-template]: https://github.com/Kapoorlabs-CAPED/cookiecutter-template
{% if cookiecutter.github_repository_url != 'provide later' %}
[file an issue]: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.package_name}}/issues
{% endif %}
[caped]: https://github.com/Kapoorlabs-CAPED/
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
