##
# Drop all listener from a SOFA file except for those between indexes IR_TO_KEEP_MIN and IR_TO_KEEP_MAX
# Currently, indexes are hardcoded to 189 and 192 for the Tindari SOFA and will keep just 3 positions

# Usage:
# ? python 1-drop_listenerPositions.py --input "D:/develop-farina-proj/MATRICES(hrtf-and-SOFA)/SOFA/ambix_o7_test.sofa" --output "D:/develop-farina-proj/MATRICES(hrtf-and-SOFA)/SOFA/ambix_o7_test_3listeners.sofa" --verbose
##


IR_TO_KEEP_MIN = 189
IR_TO_KEEP_MAX = 192
assert IR_TO_KEEP_MIN < IR_TO_KEEP_MAX

import sofar, os,sys,argparse, numpy as np


# take --in as input (string, path to sofa file) and --out as output (string, path to sofa file)

# argparse
parser = argparse.ArgumentParser(description='Modify number of channels and IR length in SOFA')
parser.add_argument('--input',              '-i', type=str, help='Path to input SOFA file')
parser.add_argument('--output',             '-o', type=str, help='Path to output SOFA file')
parser.add_argument('--verbose',            '-v', action='store_true', help='Print verbose information')
args = parser.parse_args()

# Check if --sofa is provided
if args.input is None:
    print('Please provide a path to a SOFA file using --input')
    sys.exit()
if args.output is None:
    print('--out argument was not provided, so only input sofa information will be printed')
elif os.path.exists(args.output) or os.path.exists(args.output+'.sofa'):
    print('Output file already exists. Please provide a different name')
    sys.exit()
elif not os.path.exists(os.path.dirname(os.path.abspath(args.output))):
    print('Output directory does not exist')
    sys.exit()

# Check if file exists
if not os.path.exists(args.input):
    print('File not found')
    sys.exit()

SOFA_PATH = args.input

sofafile = sofar.read_sofa(SOFA_PATH, verify=False, verbose=True)

# sofafile.add_missing()
# sofafile.add_attribute('ListenerView_Units', 'metre') #, dtype='string', dimensions=None)
# sofafile.add_attribute('SourceView_Units', 'metre')

# sofafile.verify()

# Print length of IRs (Dimension N)
print('File: "%s"'%(os.path.basename(SOFA_PATH)))

print('Reading dimensions from input SOFA file...')
input_dimensions = {
        'R': int(sofafile.get_dimension('R')),
        'N': int(sofafile.get_dimension('N')),
        'E': int(sofafile.get_dimension('E')),
        'M': int(sofafile.get_dimension('M')),
        'I': int(sofafile.get_dimension('I'))
    }
print('Done, Dimensions:')


print("Ir Length",input_dimensions['N'])
print("Num Channels",input_dimensions['R'])
nch = int(input_dimensions['R'])
if np.sqrt(nch) == int(np.sqrt(nch)):
    print("\tPotential Ambisonics IRs of %d order"%(int(np.sqrt(nch))-1))
print("Num Sources",input_dimensions['E'])
print("Num Listeners",input_dimensions['M'])
# print("Whatisthis I",input_dimensions['I'])
print()

del SOFA_PATH # Prevent accidental usage of input path


# print(args.verbose)

printVerbose = lambda *cargs, **ckwargs: print(*cargs, **ckwargs) if args.verbose else None


if args.output is not None:

    # Create new sofa
    # new_sofa = sofar.Sofa(convention='SingleRoomSRIR') # _1.0?
    import copy
    new_sofa = copy.deepcopy(sofafile)


    ir_shape = (input_dimensions['R'], input_dimensions['N'])
    # print('IR_DIMENSIONS =',ir_shape)

    # M = n_listeners
    # R = n_ch
    # N = n_samples

    for n_listeners in range(input_dimensions['M']):
        if n_listeners >= IR_TO_KEEP_MIN and n_listeners < IR_TO_KEEP_MAX:
            print("Keeping IR for listener %d"%(n_listeners))
            continue
        sofafile.Data_IR[n_listeners, : , :] = np.zeros(input_dimensions['R'],input_dimensions['N'])










#     # Apply modified IRs    
#     new_sofa.Data_IR = new_irs
    new_sofa.verify()
    # Now print dimensions
    print('\n+------------------------+')
    print('New IR shape:', new_sofa.Data_IR.shape)
    print('New number of channels (R):', new_sofa.get_dimension('R'))
    print('New IR length (N):', new_sofa.get_dimension('N'))
    print('New number of sources (E):', new_sofa.get_dimension('E'))
    print('New number of listeners (M):', new_sofa.get_dimension('M'))
    print('+------------------------+')

    
    sofar.write_sofa(filename= args.output, sofa= new_sofa, compression=0)


else:
    print('Output file was not provided, so sofa object will not be saved')


