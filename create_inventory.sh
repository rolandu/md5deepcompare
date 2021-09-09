#!/bin/bash

usage() {
    echo "Usage:"
    echo "$0 <directory you want to create an inventory for> <output file name>"
    echo ""
    echo "Example:"
    echo "$0 \"/home/username/some_dir/\" \"some_dir.md5\""
}

# Check number of arguments
if [[ ! $# -eq 2 ]]
then
    echo "Fatal error: Wrong number of arguments."
    usage
	exit 1
fi

TARGET="$1"
OUTPUT_FILE="$2"

echo "Creating inventory for \"$TARGET\"."

if [ ! -d "$TARGET" ]
then
    echo "Fatal error: Directory $TARGET does not exist."
    usage
    exit 1
fi

# It is important that the paths look the same, therefore first `cd` into the directory that you would like to compare and then use `md5deep -r -l` (`-r` is for recursive, `-l` is for relative paths.)

( cd "$TARGET"; md5deep -r -l . ) > "$OUTPUT_FILE"

echo "Done. Saved inventory to \"$OUTPUT_FILE\"."
