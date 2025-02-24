"""
Use this examples like:

tiled serve pyobject --public tiled.examples.nexus:catalog

To serve a different URL from the example hard-coded here, use the config:

```
# config.yml
authentication:
    allow_anonymous_access: true
catalogs:
    - path: /
      catalog: tiled.examples.nexus:Catalog
      args:
          url: YOUR_URL_HERE
```

tiled serve config config.yml
"""
import io

import h5py
import httpx
from tiled.readers.hdf5 import HDF5Reader


def Catalog(url):
    # Download a Nexus file into a memory buffer.
    buffer = io.BytesIO(httpx.get(url).content)
    # Access the buffer with h5py, which can treat it like a "file".
    file = h5py.File(buffer, "r")
    # Wrap the h5py.File in a Catalog to serve it with Tiled.
    return HDF5Reader(file)


EXAMPLE_URL = "https://github.com/nexusformat/exampledata/blob/master/APS/EPICSareaDetector/hdf5/AgBehenate_228.hdf5?raw=true"  # noqa
catalog = Catalog(EXAMPLE_URL)
