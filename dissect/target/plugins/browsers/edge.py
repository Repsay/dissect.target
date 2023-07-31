from dissect.target.helpers.descriptor_extensions import UserRecordDescriptorExtension
from dissect.target.helpers.record import create_extended_descriptor
from dissect.target.plugin import Plugin, export
from dissect.target.plugins.browsers.browser import (
    GENERIC_DOWNLOAD_RECORD_FIELDS,
    GENERIC_EXTENSION_RECORD_FIELDS,
    GENERIC_HISTORY_RECORD_FIELDS,
    BrowserPlugin
)
from dissect.target.plugins.browsers.chromium import ChromiumMixin


class EdgePlugin(ChromiumMixin, BrowserPlugin):
    """Edge browser plugin."""

    __namespace__ = "edge"
