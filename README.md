# sliCERR
An interface between 3DSlicer and CERR which allows the use of CERR functionality from 3DSlicer.

## Requirements

* 3DSlicer v4.11: https://download.slicer.org/
  * Slicer Jupyter extension installed via Slicer's Extension Manager
  * Optional: Python3 environment with jupyterlab
* GNU Octave v6.3: https://www.gnu.org/software/octave/download
  * Additional [Octave Forge](https://wiki.octave.org/Category:Octave_Forge) packages: io, statistics, image
* CERR Computational Environment for Radiological Research https://github.com/cerr/CERR

## Installation steps

* Install GNU Octave v6.3+
  * Open Octave and install additional packages at the command line: `pkg install -forge io; pkg install -forge statistics; pkg install -forge image`
* Install 3DSlicer v4.11+
  * Open the Slicer Python Interpreter
  * Install the oct2py bridge via the Slicer CLI `pip_install('oct2py')`
  * Add the Slicer Jupyter extension via the Slicer Extension Manager
* Clone the CERR GitHub repository and checkout the `octave_dev` branch
