all: sxiv

sxiv: sxiv.d/config.h
	make all -C sxiv.d
	cp sxiv.d/sxiv sxiv

sxiv.d/config.h: sxiv.d/config.def.h sxiv.patch
	cp sxiv.d/config.def.h sxiv.d/config.h
	patch sxiv.d/config.h sxiv.patch

sxiv.d/config.def.h: sxiv.d/.git

sxiv.d/.git:
	git submodule init
	git submodule update

clean:
	git submodule deinit sxiv.d
	rm -f sxiv
