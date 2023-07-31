from dissect.target.helpers.descriptor_extensions import UserRecordDescriptorExtension
from dissect.target.helpers.record import create_extended_descriptor
from dissect.target.plugin import Plugin, export
from dissect.target.plugins.browsers.browser import (
    GENERIC_DOWNLOAD_RECORD_FIELDS,
    GENERIC_EXTENSION_RECORD_FIELDS,
    GENERIC_HISTORY_RECORD_FIELDS,
    BrowserPlugin,
)
from dissect.target.plugins.browsers.chromium import ChromiumMixin


class EdgePlugin(ChromiumMixin, BrowserPlugin):
    """Edge browser plugin."""

    __namespace__ = "edge"

    DIRS = [
        # Linux
        ".config/microsoft-edge/Default/",
        ".var/app/com.microsoft.Edge/config/microsoft-edge/Default",
        # Windows
        "AppData/Local/Microsoft/Edge/User Data/Default",
        # Macos
        "Library/Application Support/Microsoft Edge/Default",
    ]
    BrowserDownloadRecord = create_extended_descriptor([UserRecordDescriptorExtension])(
        "browser/edge/download", GENERIC_DOWNLOAD_RECORD_FIELDS
    )
    BrowserExtensionRecord = create_extended_descriptor([UserRecordDescriptorExtension])(
        "browser/edge/extension", GENERIC_EXTENSION_RECORD_FIELDS
    )
    BrowserHistoryRecord = create_extended_descriptor([UserRecordDescriptorExtension])(
        "browser/edge/history", GENERIC_HISTORY_RECORD_FIELDS
    )
