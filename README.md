# Euclidean-algorithm
Euclidean algorithm calculator in Python

## Usage:
```bash
python3 euclid.py -h
usage: euclid.py [-h] [a] [b]

Euclidean Algorithm Calculator by Simon Possegger

positional arguments:
  a           Number a
  b           Number b

optional arguments:
  -h, --help  show this help message and exit
```

### Example:
```bash
python3 euclid.py 3600 767
i       -1       0       1       2       3       4       5       6       7       8       9
ai       1       0       1      -1       3      -10      13     -49      62     -235     767 
bi       0       1      -4       5      -14      47     -61      230    -291     1103   -3600
qi                       4       1       2       3       1       3       1       3       3   
ri       3600    767     532     235     62      49      13      10      3       1       0   

ggT( 3600, 767) =  1
```