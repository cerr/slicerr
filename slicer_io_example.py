#add following lines to user's $HOME/.slicerrc.py slicer startup file
import os
octavepath = 'C:/Octave/Octave-5.2.0/mingw64/bin/octave-cli.exe'
os.environ['OCTAVE_EXECUTABLE'] = octavepath
os.environ['PATH'] = octavepath + ';' + os.environ['PATH']


#execute in Slicer Python CLI
import numpy as np

#Get volume node from MRML scene
volumeNode = slicer.util.getNode('*CT*')
#or
volumeNode = slicer.app.layoutManager().sliceWidget("Red").sliceLogic().GetBackgroundLayer().GetVolumeNode()

#Get 3x3 voxel matrix from volume node
imgVolume = np.copy(slicer.util.arrayFromVolume(volumeNode))

#Origin, image spacing
imgOrigin = volumeNode.GetOrigin()
imgSpacing = volumeNode.GetSpacing()

#Get affine matrix with direction cosines, pixdim, origin
imgMatrixVtk = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(imgMatrixVtk)

imgMatrix = np.eye(4)
imgMatrixVtk.DeepCopy(imgMatrix.ravel(),imgMatrixVtk)

imgData = volumeNode.GetImageData()
dtype = imgData.GetScalarSize()



from slicer.util import pip_install
pip_install('oct2py')

from oct2py import octave
from oct2py import Struct

localPathToCERR = 'C:/Users/Eve/Desktop/Dev/CERR_master/CERR'
octave.addpath(octave.genpath(localPathToCERR))

##start your CERR calls
infoS = Struct()
infoS.Offset = imgOrigin #is this different from the origin?
infoS.PixelDimensions = imgSpacing
infoS.Dimensions = imgVolume.shape
scanOffset = 0
scanName = 'slicer_import'

planC = octave.mha2cerr(infoS, imgVolume,scanOffset,scanName)


##set up segmentation nodes
segLabelString = 'LUNG_R'
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", segLabelString)
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
