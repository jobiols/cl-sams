#!/usr/bin/env bash
##############################################################################
# Genera la documentacion de los modulos, requiere la instalacion de oca
# maintainers tools
# https://github.com/OCA/maintainer-tools
#
oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name cl-sams \
	--branch 11.0 \
	--addons-dir "$PWD" \
	--gen-html
