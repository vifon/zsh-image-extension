DESCRIPTION
===========

`zsh-image-selector` allows to graphically select the image files to add to the
command line (as some command's arguments perhaps). Think of it as a tab
completion for the images.

ACKNOWLEDGMENTS
===============

To display images I've used the excellent
[sxiv](https://github.com/muennich/sxiv) image viewer written by Bert Muennich
as it is great, small and hackable. ;)

USAGE
=====

To select the images from the current directory, just press C-x C-i (i.e. ctrl+x
and then ctrl+i). You can change that key by setting the `IMAGE_SELECTOR_KEY`
variable before sourcing this plugin.

If there is a path before the cursor, is is used as a prefix (or just directory)
of all the files to match. Only the files with that prefix will be diplayed for
selection.

In the sxiv window press 'm' (by default; just a key bound to the
`it_toggle_image_mark` sxiv function) to select/deselect the focused
file. Additionally you can use all the regular sxiv keys (see its manpage).

INSTALLATION
============

The first way
------------

Just source the `image-selector` file in your `zshrc`.

Pros:

- simple and easy,
- you will be using the sxiv installed in your system.

Cons:

- only newer sxiv versions are supported (commit `fb6e4bd` onwards),
- possibly incompatible config,
- possible future incompatibility,
- you need sxiv installed.

The second way
------------

Run `make` to download the sxiv source and compile it, and then source the
`image-selector` file like in the first way. You can provide your own `config.h`
and recompile sxiv (by running `make` again).

Pros:

- you will be using the compatible and tested sxiv version and config,
- allows custom sxiv configuration for use with this plugin.

Cons:

- the bundled sxiv may become relatively old in the future (updating it is not a
  priority),
- may need to be recompiled from time to time (shared libraries etc.),
- needs the build dependencies of sxiv.

SEE ALSO
========

sxiv(1)

AUTHOR
======

Wojciech 'vifon' Siewierski < wojciech dot siewierski at gmail dot com >

COPYRIGHT
=========

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
