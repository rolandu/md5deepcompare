# md5deepcompare

## Use case

I use this script for two situations:

1. Two or more directories that *should* contain identical files, but you are not sure (e.g. problems during a backup/transfer). In this situations I want to compare the whole directory tree.
2. You want to make sure that a directory is unchanged from an earlier state. 

## Approach

Using `md5deep` we create a file containing the md5-hashes of all the files in the directory. Then we compare whether both directories contain the same files with the same hashes.

## Howto

### Installation

You only need bash and `md5deep`. 

If you have apt, you can probably use:

	apt install md5deep

### Step 1: Create md5deep log

This uses `md5deep` to create a log file for a given directory. Use this on any directory you want to compare.

	./create_inventory.sh test/directory\ 1/ 1.md5

### Step 2: Compare the logs

Now we want to compare the logs. Does directory 2 contain everything from directory 1?



## Why not use...

### diff

Although diff serves a different function, I had problems due to differing metadata and symlinks. Therefore I decided to only compare names and hashes.

