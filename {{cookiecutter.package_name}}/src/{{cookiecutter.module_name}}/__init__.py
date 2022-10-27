{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}

{% if cookiecutter.include_sample_data_plugin == 'y' -%}
from ._sample_data import make_sample_data
{% endif %}
__all__ = (
   
   {% if cookiecutter.include_sample_data_plugin == 'y' -%}
    "make_sample_data",
    {% endif %}

)
