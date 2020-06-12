"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from cdb.main import ContainerDatabase


def main(args, extra):

    # Create a Container database
    db = ContainerDatabase(path=args.path)
    db.generate(
        output=args.output, template=args.template, force=args.force, func=args.function
    )
