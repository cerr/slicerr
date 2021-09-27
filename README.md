# sliCERR
An interface between 3DSlicer and CERR which allows the use of CERR functionality from 3DSlicer.

## Requirements

* 3DSlicer v4.11: https://download.slicer.org/
  * Slicer Jupyter extension installed via Slicer's Extension Manager
  * Optional: Python3 environment with jupyterlab
* GNU Octave v6.3: https://www.gnu.org/software/octave/download
  * Additional Octave Forge packages: io, statistics, image
* CERR Computational Environment for Radiological Research https://github.com/cerr/CERR

## Installation steps

* Install GNU Octave
* Install 3DSlicer
  * Open the Slicer Python Interpreter
  * Install the oct2py bridge via the Slicer CLI `pip_install('oct2py')`
  * Add the Slicer Jupyter extension via the Slicer Extension Manager
* Clone the CERR GitHub repository and checkout the `octave_dev` branch
