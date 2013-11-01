DESCRIPTION
===========

`zsh-image-selector` is a zsh plugin that allows to graphically select the image
files to add to the command line (as some command's arguments perhaps). Think of
it as a tab completion for the images.

ACKNOWLEDGMENTS
===============

To display images I've used the excellent
[sxiv](https://github.com/muennich/sxiv) image viewer written by Bert Muennich
as it is great, small and hackable. ;)

USAGE
=====

IMAGE SELECTION
---------------

To select the images from the current directory, just press C-x C-i (i.e. ctrl+x
and then ctrl+i). You can change that key by setting the `IMAGE_SELECTOR_KEY`
variable before sourcing this plugin.

If there is a path before the cursor, only the files matching it will be offered
for selection. It can be either a directory or a prefix (or prefix in a
directory).

In the sxiv window which will appear, press 'm' (by default; just a key bound to
the `it_toggle_image_mark` sxiv function) to select/deselect the focused
file. Additionally you can use all the regular sxiv keys (see its manpage).

IMAGE PREVIEW
-------------

There is an experimental image preview feature which displays the images from
the argument list **in the terminal window**. You need `w3m` installed along
with the `w3mimgdisplay` program. It is confirmed to work in `urxvt` and
`xterm`. Activate it with C-x C-o (customizable via the `IMAGE_SELECTOR_KEY`
variable). Press any key to hide the previews.

INSTALLATION
============

The first way
-------------

Just source the `image-selector` file in your `zshrc`.

You'll need the sxiv image viewer (I know, I know, it's dumb to say "the simple
X image viewer image viewer"...) installed.

**It's quite likely it will not work due to the incompatible (too old) sxiv
  version. Try the second way in this case.**

Pros:

- simple and easy,
- you will be using the sxiv installed in your system (which may be newer than
  the bundled version).

Cons:

- you will be using the sxiv installed in your system (which may be older than
  the bundled version),
- only newer sxiv versions are supported (commit `fb6e4bd` onwards),
- possibly incompatible config,
- possible future incompatibility,
- you need sxiv installed.

The second way
--------------

Run `make` to download the sxiv source and compile it, and then source the
`image-selector` file like in the first way. You can provide your own `config.h`
and recompile sxiv (by running `make` again).

Pros:

- you will be using the compatible and tested sxiv version and config,
- only slightly less simple and easy ;)

Cons:

- the bundled sxiv may become relatively old in the future (updating it is not a
  priority),
- may need to be recompiled from time to time (shared libraries etc.),
- needs the build dependencies of sxiv.

KNOWN ISSUES AND TROUBLESHOOTING
================================

All images are selected every time
----------------------------------

You are using an old sxiv version which does not support the mark command. Try
the second installation method to compile the compatible version.

Image previews are too big/too small
------------------------------------

It should be handled automatically but if it isn't, there is a config section on
top of the `image-preview` script, so you can adjust it for your screen
size. (the default was set on 1680x1050 and should autoscale)

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
