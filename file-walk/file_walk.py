import os

def list_files_driver(output_format,startpath,verbose):
    if output_format == 'csv':
        list_files_csv(startpath,verbose)
    elif output_format == 'txt':
        list_files_txt(startpath,verbose)

def list_files_txt(startpath, verbose):

    if startpath == '': startpath = os.getcwd()
    output = []
    depth_limit = 2
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level > depth_limit:
            pass
        else:
            indent = (' ' * 7 * (level))
            try:
                fol = '{}[{}]/--|'.format(indent, os.path.basename(root))
                output.append(fol)
                if verbose == True: print(fol)
            except:
                emsg = '!!!...PATHDEEPER...!!!'
                output.append('{}{}'.format(indent,emsg))
                if verbose == True:print(emsg)
            #subindent = ' ' * (4 * (level + 1)) + ( ' ' * len(fol))
            subindent = ( ' ' * (len(fol) - 1))

            for f in files:
                try:
                    fil = '{}|--{}'.format(subindent, f)
                    output.append(fil)
                    if verbose == True:print(fil)
                except:
                    emsg = '!!!...FILEDEEPER...!!!'
                    output.append('{}{}'.format(indent,emsg))
                    if verbose == True:print('!!!...FILEDEEPER...!!!')
    with open('file_structure.txt','w') as f:
        for line in output:
            f.write(line + '\n')


def list_files_csv(startpath, verbose):

    if startpath == '': startpath = os.getcwd()
    output = []
    depth_limit = 2
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level > depth_limit:
            pass
        else:
            indent = (',' * (level))
            try:
                fol = '{}[{}]/'.format(indent, os.path.basename(root))
                output.append(fol)
                if verbose == True: print(fol)
            except:
                emsg = '!!!...PATHDEEPER...!!!'
                output.append('{}{}'.format(indent,emsg))
                if verbose == True:print(emsg)
            #subindent = ' ' * (4 * (level + 1)) + ( ' ' * len(fol))
            subindent = ( ',' * (level+1))

            for f in files:
                try:
                    fil = '{}{}'.format(subindent, f)
                    output.append(fil)
                    if verbose == True:print(fil)
                except:
                    emsg = '!!!...FILEDEEPER...!!!'
                    output.append('{}{}'.format(indent,emsg))
                    if verbose == True:print('!!!...FILEDEEPER...!!!')
    with open('file_structure.csv','w') as f:
        for line in output:
            f.write(line + '\n')




cwd = os.getcwd()
wd = input('What is the structure directory you would like to walk? ... ')
verbose = input('Would you like to print?   y/n')
if verbose == 'y':
    verbose = True
else:
    verbose = False
list_files_driver('csv',wd,verbose)
print('...Done...')
