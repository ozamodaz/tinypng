#### Batch compressing / resizing images using tinypng / tinyjpg
Requirements:
```
pip install tinify
```
Get your API Key at https://tinypng.com/developers
(The first 500 compressions each month are free)
And set it in the top of script:
```
 tinify.key = 'YOUR API KEY'
```
----
Default behavior is to compress all image files in the same directory as the script is. Compressed images will be saved to './compressed' directory. The directory will be created if needed. If not empty, script will skip theese filenames, considering them as already comressed.

you may like to tune resize options for your needs
```
resized = source.resize(
        method="scale",
        width=1000,
        )
```
resizing methods and other cool stuff described here: https://tinypng.com/developers/reference/python
