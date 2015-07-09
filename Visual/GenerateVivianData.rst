Generate VIVIAN Backend Data
============================

FileMan Global Data Parser
---------------------------

From the VistA Code repository:

https://github.com/OSEHRA-Sandbox/VistA

Branch: VistADataParse

From the **Utilities/Dox/PythonScripts** directory run::

  python FileManGlobalDataParser.py -h

  usage: FileManGlobalDataParser.py [-h] -mr MREPOSITDIR -pr PATCHREPOSITDIR
                                    [-outdir OUTDIR] [-all]
                                    fileNos [fileNos ...]

  FileMan Global Data Parser

  positional arguments:
    fileNos               FileMan File Numbers

  optional arguments:
    -h, --help            show this help message and exit
    -outdir OUTDIR        top directory to generate output in html
    -all                  generate all dependency files as well

  Initial CrossReference Generator Arguments:
    Argument for generating initial CrossReference

    -mr MREPOSITDIR, --MRepositDir MREPOSITDIR
                          VistA M Component Git Repository Directory
    -pr PATCHREPOSITDIR, --patchRepositDir PATCHREPOSITDIR
                          VistA Git Repository Directory


To generate Backend Data for HL7/RPC as well as VistA Menus.d

Please run::

  python FileManGlobalDataParser.py -outdir </path/to/outdir> -all 
                                    -mr </path/to/VistA-M/repository> 
                                    -pr </path/to/VistA/repository>
                                    <101> <8994> <19>

Where 101, 8994, 19 are the fileman numbers for protocol, RPC and options respectively.

Please also replace the path accordingly.


Create Packages.csv
-------------------

From the Scripts repository run ::

  python PopulatePackages.py 


Link backend data with VIVIAN
-----------------------------

Get VIVIAN Code repository:

https://github.com/OSEHRA-Sandbox/Product-Management/tree/master/Visual

In the Visual directory of the VIVIAN repository, create a link named **files** that
points to the outdir created above.

Copy **Packages.csv** (created above) to the Visual directory.

Update **PackageCategories.json** if needed.


Populate menus directory
------------------------

Delete all files in the **Visual/menus** directory.

Move all the VistAMenu-\*.json files from **Visual/files** to **Visual/menus**.

Next, run a Python script to create menu_autocomplete.json.

::

  python menu_autocomplete_gen.py 

Requires:  Visual/menus

Creates: menu_autocomplete.json

Used By: vista_menus.php


Create PackageInterface.csv
---------------------------

::

  python pkg_interface_gen.py 

Requires:  Visual/files 

Creates: PackageInterface.csv

Used By: pkgcsv_to_json.py


Create packages.json
---------------------
::

  python pkgcsv_to_json.py

Requires: Packages.csv, PackageInterface.csv, PackageCategories.json

Creates: packages.json

Used By: prod_visual.html

Create pkgdep.json
------------------

Used by: package_dep_bar_chart.html, package_stats_chart.html,
pkgdep_chart_data.py, vista_pkg_dep.php, vistadep.html


DSS vxVistA
============

Currently the Visualization for vxVistA lives in a separate branch:

https://github.com/OSEHRA-Sandbox/Product-Management/tree/vxVistA-2013.0

Follow the same workflow above to generate the backend data for vxVistA,
remember to change the VistA-M repository to the one point to vxVistA: https://github.com/OSEHRA/vxVistA-M