zsh-image-extension
===================

DESCRIPTION
-----------

`zsh-image-extension` provides the image viewing capabilities to zsh. It allows
previewing images listed on the command line and graphically selecting the
images to append to it.

USAGE
-----

**Image preview**

You can preview the images listed in the command line in the terminal window by
pressing ctrl+x ctrl+o (i.e. ctrl+x and then ctrl+o). Press any key dismiss. If
there are too many images to display, any key other than 'q' will display the
next image portion.

May not work with all the terminals. Confirmed to work with `urxvt`, `xterm` and
the Linux tty.

It needs the `w3mimgdisplay` utility usually provided by `w3m` or `w3m-img`
package.

The activation sequence may be customized by setting the
`IMAGE_EXTENSION_PREVIEW_KEY` variable prior to loading this plugin.


**Image selection**

To graphically select images to append to the command line, press ctrl+x
ctrl+o. A new window with the thumbnails will appear. Use arrow keys and/or hjkl
to navigate, Enter to zoom in/out and 'm' to mark files to be added (a small
asterisk/star should appear in the lower left corner).

If there is a path before the cursor, the files in that directory will be
listed. The current directory is used otherwise.

Please refer to the [sxiv documentation](https://github.com/muennich/sxiv/blob/master/README.md) for
more advanced usage.

The activation sequence may be customized by setting the
`IMAGE_EXTENSION_SELECTION_KEY` variable prior to loading this plugin.

INSTALLATION
------------

Run `make` to download the `sxiv` source and compile it, and then source
(i.e. add the `source path/to/file` line to your `zshrc`) the
`zsh-image-extension`. You can provide your own `config.h` and recompile `sxiv`
(by running `make` again).

If you have `sxiv` installed, you may omit the most of it and only source the
`zsh-image-extension` file but I cannot guarantee your `sxiv`'s compatilibity (the
first compatible commit -- `fb6e4bd`).

DEPENDENCIES
------------

* `sxiv` (automatically provided) for image selection
* `w3m` (`w3m-img` on Debian, Ubuntu, etc.) for image preview

KNOWN ISSUES AND TROUBLESHOOTING
--------------------------------

**All images are selected every time**

You are using an old `sxiv` version which does not support the mark command. Run
`make` to compile the compatible version.

**Image previews are too big/too small**

It should be handled automatically but if it isn't, there is a config section on
top of the `image-preview.py` script, so you can adjust it for your screen
size. (the default was set on 1680x1050 and should autoscale unless in tty)

ACKNOWLEDGMENTS
---------------

To list and select images I've used the excellent
[sxiv](https://github.com/muennich/sxiv) image viewer written by Bert Muennich
as it is great, small and hackable. ;)

Image previewing is handled by the `w3mimgdisplay` utility provided by `w3m`.

SEE ALSO
--------

sxiv(1)

AUTHOR
------

Wojciech 'vifon' Siewierski < wojciech dot siewierski at gmail dot com >

COPYRIGHT
---------

Copyright (C) 2013  Wojciech Siewierski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
