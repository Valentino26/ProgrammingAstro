In [computing](https://en.wikipedia.org/wiki/Computing "Computing"), **Deflate** (stylized as **DEFLATE**, and also called **Flate** is a [lossless](https://en.wikipedia.org/wiki/Lossless_compression "Lossless compression") [data compression](https://en.wikipedia.org/wiki/Data_compression) [file format](https://en.wikipedia.org/wiki/File_format "File format") that uses a combination of [LZ77](https://en.wikipedia.org/wiki/LZ77_and_LZ78 "LZ77 and LZ78") and [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding "Huffman coding"). It was designed by [Phil Katz](https://en.wikipedia.org/wiki/Phil_Katz "Phil Katz"), for version 2 of his [PKZIP](https://en.wikipedia.org/wiki/PKZIP "PKZIP") archiving tool. Deflate was later specified in [RFC](https://en.wikipedia.org/wiki/Request_for_Comments "Request for Comments") 1951 (1996)

Katz also designed the original algorithm used to construct Deflate streams. This algorithm was [patented](https://en.wikipedia.org/wiki/Software_patent "Software patent") as [U.S. patent 5,051,745](https://patents.google.com/patent/US5051745), and assigned to [PKWARE, Inc.](https://en.wikipedia.org/wiki/PKWARE,_Inc. "PKWARE, Inc.") As stated in the RFC document, an algorithm producing Deflate files was widely thought to be implementable in a manner not covered by patents. This led to its widespread use – for example, in [gzip](https://en.wikipedia.org/wiki/Gzip "Gzip") compressed files and [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics "Portable Network Graphics") image files, in addition to the [ZIP](https://en.wikipedia.org/wiki/ZIP_(file_format) "ZIP (file format)") file format for which Katz originally designed it. The patent has since expired.

A Deflate stream consists of a series of blocks. Each block is preceded by a 3-[bit](https://en.wikipedia.org/wiki/Bit "Bit") header:

- First bit: Last-block-in-stream marker:
    - `1`: This is the last block in the stream.
    - `0`: There are more blocks to process after this one.
- Second and third bits: Encoding method used for this block type:
    - `00`: A stored (a.k.a. raw or literal) section, between 0 and 65,535 bytes in length
    - `01`: A _static Huffman_ compressed block, using a pre-agreed Huffman tree defined in the RFC
    - `10`: A _dynamic Huffman_ compressed block, complete with the Huffman table supplied
    - `11`: Reserved—don't use.

The _stored_ block option adds minimal overhead and is used for data that is incompressible.

Most compressible data will end up being encoded using method `10`, the _dynamic Huffman_ encoding, which produces an optimized Huffman tree customized for each block of data individually. Instructions to generate the necessary Huffman tree immediately follow the block header. The static Huffman option is used for short messages, where the fixed saving gained by omitting the tree outweighs the percentage compression loss due to using a non-optimal (thus, not technically Huffman) code.

Compression is achieved through two steps:

- The matching and replacement of duplicate strings with pointers.
- Replacing symbols with new, weighted symbols based on the frequency of use.