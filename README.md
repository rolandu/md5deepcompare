# md5deepcompare

## Use case

Different directories that *should* contain identical files, but you are not sure.

## Approach

Using `md5deep` we create a file containing the md5-hashes of all the files in the directory. Then we compare whether both directories contain the same files with the same hashes.

## Howto

...

## Why not use...

### diff

Although diff serves a different function, I had problems due to differing metadata and symlinks. Therefore I decided to only compare names and hashes.

