#!/bin/bash

sudo apt update
sudo apt install pandoc

pandoc -f markdown+rebase_relative_paths+gfm_auto_identifiers --toc -s -t gfm tickets/**/*.md -o output.md   