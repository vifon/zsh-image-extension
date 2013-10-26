DESCRIPTION
===========

`zsh-image-selector` allows to graphically select the image files to add to the
command line (as some command's arguments perhaps). Think of it as a tab
completion for the images.

INSTALLATION
============

Copy or link this directory to `~/.zsh-image-selector/`. Run `make` and then
just source the `~/.zsh-image-selector/image-selector` file in your `zshrc`.

You can use some other directory in more recent versions but it is only slightly
tested.

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

In the sxiv window press Ctrl+Enter to select the focused file. Additionally you
can use all the regular sxiv keys (see its manpage).

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
