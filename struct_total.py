#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import os
         
def __mkdir_out_filefolder():
    try:
        myfile = os.getcwd()+'\\out_dir'
        if not os.path.exists(myfile):
            os.mkdir(myfile)
    except:
        print('file not exist or corupted')
        sys.exit()
        
def __get_output_file_name(out_file_name):
    try:       
        out_file_name = out_file_name.lower()
        out_file_name = 'out_dir\\' + out_file_name + '_'+ 'struct_interface.h'    
        return out_file_name     
    except:
        print('len of line is 1 ')
        sys.exit() 
       
def __wirte_list_to_file(list_out,file_name):
    try:
        with open(file_name, 'w+') as file:
            file_name = file_name.split('\\')
            file_name = file_name[-1]
            file_name = file_name.replace('.','_')
            file_name1 = '#ifndef ' + file_name.upper()+'\n'
            file_name2 = '#define ' + file_name.upper()+'\n'     
            common_header = '#include \"common_module_struct_interface.h\"\n'
            file.write(file_name1)
            file.write(file_name2)
            #file.write(common_header)
            file.write('\n'.join(list_out)) 
            file.write('\n#endif\n')
    except:
        print('file not exist or corupted')
        sys.exit()
 
def __dir_list_process_struct(sub_dir_list,file_name):
    try:
        sub_dir_all = []
        str1 = 'typedef struct _AAAAA_struct_t\n{'
        str2 = file_name.lower()
        str3 = str1.replace('AAAAA',str2)
        sub_dir_all.append(str3)
        for sub_dir in sub_dir_list[1:]: 
            sub_dir = sub_dir.lower()    
            sub_dir = '    sftst_' + sub_dir + '_t    ' + sub_dir + ';'
            sub_dir_all.append(sub_dir) 
        str1 = '}AAAAA_struct_t;\nextern    AAAAA_struct_t    AAAAA_struct;'
        str2 = file_name.lower()
        str3 = str1.replace('AAAAA',str2)
        sub_dir_all.append(str3)      
        return sub_dir_all
    except:
        print('file not exist or corupted')
        sys.exit()

def __dir_list_process_header(sub_dir_list,file_name):
    try:
        sub_dir_all = []
        for sub_dir in sub_dir_list[1:]: 
            sub_dir = sub_dir.lower()    
            sub_dir = '#include "tst_' + sub_dir + '_struct_interface.h"'
            sub_dir_all.append(sub_dir) 
        return sub_dir_all
    except:
        print('file not exist or corupted')
        sys.exit()

def __dir_list_process_enum(sub_dir_list):
    try:
        sub_dir_all = []
        #str1 = '#if 0\ntypedef struct _localtimestamp{\n    sync_time_uint64_t sec;\n    sync_time_uint64_t nsec;\n    sync_time_uint32_t flag;\n}sync_timestamp_t;\n#endif'
        #sub_dir_all.append(str1)
        str1 = 'typedef enum _SFTST_HANDLE_E\n{'
        sub_dir_all.append(str1)
        for sub_dir in sub_dir_list[1:]: 
            sub_dir = sub_dir.upper()    
            sub_dir = '    SFTST_' + sub_dir + '_E,'
            sub_dir_all.append(sub_dir) 
        str1 = '}SFTST_HANDLE_E;'       
        sub_dir_all.append(str1)      
        return sub_dir_all
    except:
        print('file not exist or corupted')
        sys.exit()		
        
def __dir_list_struct_total(sub_dir_list,file_name):
    sub_dir1 = __dir_list_process_header(sub_dir_list,file_name)
    sub_dir2 = __dir_list_process_struct(sub_dir_list,file_name)
    sub_dir_all = sub_dir1 + sub_dir2
    out_file_name = __get_output_file_name(file_name)
    __wirte_list_to_file(sub_dir_all,out_file_name)
	
def __dir_list_enum_total(sub_dir_list,file_name):
    sub_dir_all = __dir_list_process_enum(sub_dir_list)
    out_file_name = __get_output_file_name(file_name)
    __wirte_list_to_file(sub_dir_all,out_file_name)
        
def  get_struct_total(sub_dir_list):
    __mkdir_out_filefolder()     
    __dir_list_struct_total(sub_dir_list,'tst_total')
    __dir_list_enum_total(sub_dir_list,'common_tst')
                          
def main(argv=None):
    if argv is None:
        argv = sys.argv
        if len(argv) < 2:
            print('please set argv as log file')
        else:                                           
            get_struct_total(['','uss','cam'])            
            print('generate file end');            

if __name__ == "__main__":
    sys.exit(main())
 