![[Screenshot 2024-05-05 193909.png]]

> __Vector Graphics__
> 	Are a form of computer graphics in which visual images are created directly from geometric shapes defined on a Cartesian plane, such as points, lines, curves and polygons. The associated mechanisms may include vector display and printing hardware, vector data models and file formats, as well as the software based on these data models (especially graphic design software, computer-aided design, and geographic information systems). Vector graphics are an alternative to raster or bitmap graphics, with each having advantages and disadvantages in specific situations.

> __Bitmap Graphics__
> 	In [computer graphics](https://en.wikipedia.org/wiki/Computer_graphics "Computer graphics") and [digital photography](https://en.wikipedia.org/wiki/Digital_photography "Digital photography"), a **raster graphic** represents a two-dimensional picture as a rectangular matrix or grid of [pixels](https://en.wikipedia.org/wiki/Pixel "Pixel"), viewable via a [computer display](https://en.wikipedia.org/wiki/Computer_display "Computer display"), [paper](https://en.wikipedia.org/wiki/Paper "Paper"), or other display medium. A raster is technically characterized by the width and height of the image in pixels and by the number of [bits per pixel](https://en.wikipedia.org/wiki/Bits_per_pixel "Bits per pixel").Raster images are stored in [image files](https://en.wikipedia.org/wiki/Image_file "Image file") with varying [dissemination](https://en.wikipedia.org/wiki/Electronic_publishing "Electronic publishing"), [production](https://en.wikipedia.org/wiki/Raster_graphics_editor "Raster graphics editor"), [generation](https://en.wikipedia.org/wiki/3D_rendering "3D rendering"), and [acquisition formats](https://en.wikipedia.org/wiki/Raw_image_format "Raw image format").

# File Format

A PDF file is organized using ASCII characters, except for certain elements that may have binary content. The file starts with a *header* containing a *magic number* (as a readable string) and the version of the format, for example %PDF-1.7.
The format is a subset of a COS format. A COS tree file consists primarily of objects, of which there are nine types:
* Boolean
* Real numbers
* Integers
* Strings, enclosed within parentheses or represented as hexadecimal within single angle brackets. Strings may contain 8-bit characters
* Names, starting with a forward slash
* Arrays
* Dictionaries
* Streams, usually containing large amounts of optionally compressed binary data, preceded by a dictionary and enclosed between the *stream* and *endstream* keywords
* The null object
Comments using 8-bit characters prefixed with the percent sign may be inserted.

[source](https://en.wikipedia.org/wiki/PDF)

