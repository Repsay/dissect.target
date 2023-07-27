from dissect.target.helpers.descriptor_extensions import UserRecordDescriptorExtension
from dissect.target.helpers.record import create_extended_descriptor
from dissect.target.plugin import NamespacePlugin, export

RemoteAccessRecord = create_extended_descriptor([UserRecordDescriptorExtension])(
    "application/log/remoteaccess",
    [
        ("datetime", "ts"),
        ("string", "tool"),
        ("uri", "logfile"),
        ("string", "description"),
    ],
)


class RemoteAccessPlugin(NamespacePlugin):
    """General Remote Access plugin.

    This plugin groups the functions of all remote access plugins. For example,
    instead of having to run both teamviewer.remoteaccess and anydesk.remoteaccess,
    you only have to run remoteaccess.remoteaccess to get output from both tools.
    """

    __namespace__ = "remoteaccess"

    SUBPLUGINS = [
        "teamviewer",
        "anydesk",
    ]

    @export(record=RemoteAccessRecord)
    def remoteaccess(self):
        """Return Remote Access records from all Remote Access Tools.

        This plugin groups the functions of all remote access plugins. For example, instead of having to run both
        teamviewer.remoteaccess and anydesk.remoteaccess, you only have to run remoteaccess.remoteaccess to get output
        from both tools.

        Yields RemoteAccessRecords with the following fields:
           ('string', 'hostname'),
           ('string', 'domain'),
           ('datetime', 'ts'),
           ('string', 'user'),
           ('string', 'tool'),
           ('uri', 'logfile'),
           ('string', 'description')
        """
        for e in self._func("remoteaccess"):
            yield e
