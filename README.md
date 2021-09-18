# md5deepcompare

## Use case

I use this script for two situations:

1. Two or more directories that *should* contain identical files, but you are not sure (e.g. problems during a backup/transfer). In this situations I want to compare the whole directory tree.
2. You want to make sure that a directory is unchanged from an earlier state. 

## Approach

Using `md5deep` we create a file containing the md5-hashes of all the files in the directory. Then we compare whether both directories contain the same files with the same hashes.

## Requirements

- bash
- md5deep
- python3

If you have `apt`, this can usually be installed using:

`apt install md5deep python3`

## Usage

### Step 1: Create md5deep inventory

This uses `md5deep` to create a log file for a given directory. Use this on any directory you want to compare. 

The work is done by md5deep, the script only helps us so that the logs always look the same.

	./create_inventory.sh <directory> <output file>

e.g.

	./create_inventory.sh "test/directory 1/" "test/1.md5"

### Step 2: Compare the logs

Now we want to compare the logs. Does directory 2 contain everything from directory 1?

    python3 md5deepcompare.py <first md5deep output> <second md5deep output>

There is a lot of output, so you might want to redirect it to a file.

e.g.

    python3 md5deepcompare.py "test/1.md5" "test/2.md5" > md5deepcompare.log

## Why not use...

### diff

Although diff serves a similar purpose, I had problems due to differing metadata and symlinks. Therefore I decided to only compare file names and hashes.

