import ctypes
import platform
import os
import sys
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ook0', help='feature 1/K0 value (TIMS)', required=True, type=float)
    parser.add_argument('--charge', help='feature charge', required=True, type=int)
    parser.add_argument('--mz', help='feature m/z value', required=True, type=float)
    arguments = parser.parse_args()
    return vars(arguments)


def init_tdf_sdk_dll():
    if platform.system() == 'Windows':
        if platform.architecture()[0] == '64bit':
            TDF_SDK_VERSION = 'sdk2871'
            TDF_SDK_DLL_FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                 os.path.join('tdf_sdk_2871', 'win64', 'timsdata.dll'))
        elif platform.architecture()[0] == '32bit':
            TDF_SDK_VERSION = 'sdk2871'
            TDF_SDK_DLL_FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                 os.path.join('tdf_sdk_2871', 'win32', 'timsdata.dll'))
    elif platform.system() == 'Linux':
        TDF_SDK_VERSION = 'sdk2871'
        TDF_SDK_DLL_FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                             os.path.join('tdf_sdk_2871', 'linux64', 'timsdata.so'))
    else:
        print('Bruker API not found...')
        print('Exiting...')
        TDF_SDK_DLL_FILE_NAME = ''
        sys.exit(1)

    tdf_sdk_dll = ctypes.cdll.LoadLibrary(os.path.realpath(TDF_SDK_DLL_FILE_NAME))

    # Convert 1/k0 to CCS
    # Only available in SDK version 2.8.7.1 or 2.7.0
    if TDF_SDK_VERSION == 'sdk2871' or TDF_SDK_VERSION == 'sdk270':
        tdf_sdk_dll.tims_oneoverk0_to_ccs_for_mz.argtypes = [ctypes.c_double,
                                                            ctypes.c_int32,
                                                            ctypes.c_double]
        tdf_sdk_dll.tims_oneoverk0_to_ccs_for_mz.restype = ctypes.c_double

    return tdf_sdk_dll


# from timsdata.py
# Convert 1/k0 to CCS for a given charge and mz
def one_over_k0_to_ccs(ook0, charge, mz):
    bruker_dll = init_tdf_sdk_dll()
    return bruker_dll.tims_oneoverk0_to_ccs_for_mz(ook0, charge, mz)


if __name__ == '__main__':
    args = get_args()
    ccs = one_over_k0_to_ccs(args['ook0'], args['charge'], args['mz'])
    print('1/K0: ' + str(args['ook0']))
    print('Charge: ' + str(args['charge']))
    print('m/z: ' + str(args['mz']))
    print('Calculated CCS Value: ' + str(ccs) + ' \u00c5')
