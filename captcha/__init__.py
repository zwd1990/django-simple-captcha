VERSION = (0, 5, 13)


def get_version(svn=False):
    "Return the version as a human-format string."
    return ".".join([str(i) for i in VERSION])
