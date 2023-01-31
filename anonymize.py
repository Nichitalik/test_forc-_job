import pydicom
from pydicom import dcmread
import shutil
from glob import glob
import os

path_to_dicon = 'recruit\src\*'
element = ['StudyInstanceUID','SeriesInstanceUID',"SOPInstanceUID"]



def new_path(path_to):
    ds = dcmread(path_to)
    result = ''
    for el in element:
        result += str(ds[el][0:]) + '/'
    result = result[:-1]+'.dcm'
    return(result)

def list_path(file):
    result = '{} -----> new_folder/{}'.format(file, new_path(file))
    return result


def anonymize_dicom(in_path, out_path, patient_name= 'Anonymous'):
    dicom_file = pydicom.dcmread(in_path)
    dicom_file.PatientName = patient_name
    dicom_file.save_as(out_path)
    


if not os.path.exists('new_folder'):    
    os.mkdir('new_folder')
    
for slice_ in glob(path_to_dicon):
    anonymize_dicom(slice_, slice_,)
    
    path_new_file = new_path(slice_)
    layer_1, layer_2, new_file = path_new_file.split('/')
    if not os.path.exists('new_folder/'+layer_1):
        os.mkdir('new_folder/'+layer_1)
    if not os.path.exists('new_folder/'+layer_1+'/'+layer_2):
        os.mkdir('new_folder/'+layer_1+'/'+layer_2)
    target_path = open('new_folder/'+path_new_file, 'w+')
    shutil.copyfile(slice_, 'new_folder/'+path_new_file)
    
    file = open('path.txt', 'a+')
    file.write(list_path(slice_)+'\n')
    file.close()