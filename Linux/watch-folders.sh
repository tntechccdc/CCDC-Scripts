#!/bin/bash

#make sure to check aliases before use!

##########################################
# Usage:
# ./watch-folders.sh { list of folders to watch }
#
# Description:
# just runs the find command every 30 seconds on all the specified folders,
# sorting by most recent updates at the top. Highlighting any changes between instances
#
# Note: it is best to be specific with the folders you want this to watch, for example
# /usr/bin and /bin and /etc are better than say just specifying /
#
##########################################

watch -d -n 30 "find $@ -printf \"%a\t%M\t%s\t%g:%u\t%p\n\"  | sort -d | head -n 25"
