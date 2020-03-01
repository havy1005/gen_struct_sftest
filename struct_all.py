#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import os

def __read_file_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = (file.read())
            lines = lines.split('\n')        
    except:
        print('file not exist or corupted')
        sys.exit()
    return lines  
       
def __get_input_file_name(dir_name,sub_dir):
    file_list = []
    try:
        file_dir = os.getcwd() + '\\' + dir_name + '\\' + sub_dir
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.h':                                      
                    file_list.append(os.path.join(root,file))
        return file_list
    except:
        print('file not exist or corupted')
        sys.exit()
    
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
        out_file_name = 'out_dir\\' + out_file_name + '_'+ 'struct_interface_all.h'    
        return out_file_name     
    except:
        print('len of line is 1 ')
        sys.exit() 
             
def __file_line_process_not_channel(lines): 
    demo_lines_out=[]
    try:   
        str1 = '    AAAAA_16_BBBBB_LEVEL    BBBBB_LEVEL;\n    AAAAA_8_BBBBB           BBBBB;\n'
        str1 = str1 + '    uint8    BBBBB_RSV;'        
        line = lines[0]
        modulestr = line.split('\"')
        modulestr = modulestr[1]
        modulestr = modulestr.upper()        
        str1 = str1.replace('AAAAA',modulestr)
        line = lines[1]
        modulestr = line.split('\"')
        modulestr = modulestr[1]
        modulestr = modulestr.upper()
        str1 = str1.replace('BBBBB',modulestr)
        demo_lines_out.append(str1)
        return demo_lines_out     
    except:
        print('len of line is 22 ')
        sys.exit()  
        
def __file_line_process_channel(lines): 
    demo_lines_out=[]
    try:   
        str1 = '    AAAAA_16_BBBBB_LEVEL    BBBBB_LEVEL[CCCCC];\n    AAAAA_8_BBBBB           BBBBB[CCCCC];\n'
        str1 = str1 + '    uint8    BBBBB_RSV[CCCCC];'        
        line = lines[0]
        modulestr = line.split('\"')
        modulestr = modulestr[1]
        modulestr = modulestr.upper()        
        str1 = str1.replace('AAAAA',modulestr)
        line = lines[1]
        modulestr = line.split('\"')[1]
        modulestr = modulestr.split('[')[0]
        modulestr = modulestr.upper()
        str1 = str1.replace('BBBBB',modulestr)       
        line = lines[1]
        modulestr = line.split('\"')[1]
        modulestr = modulestr.split('[')[1]
        modulestr = modulestr.split(']')[0]
        modulestr = modulestr.upper()
        str1 = str1.replace('CCCCC',modulestr)       
        demo_lines_out.append(str1)
        return demo_lines_out     
    except:
        print('len of line is 22 ')
        sys.exit()  

def __file_line_process(lines): 
    demo_lines_out=[]
    try:          
        line = lines[1]
        obj = re.search(r'\.*\[\.*',line)
        if obj :
            pass
            demo_lines_out = __file_line_process_channel(lines)
        else :
            pass
            demo_lines_out = __file_line_process_not_channel(lines)            
        return demo_lines_out     
    except:
        print('len of line is 2233 ')
        sys.exit() 
       
def __wirte_list_to_file(list_out,file_name,sub_dir):
    try:
        with open(file_name, 'w+') as file:
            file_name = file_name.split('\\')
            file_name = file_name[-1]
            file_name = file_name.replace('.','_')
            file_name1 = '#ifndef ' + file_name.upper()+'\n'
            file_name2 = '#define ' + file_name.upper()+'\n'
            common_header = '#include \"common_module_struct_interface.h\"\n'           			
            file_name3 = '#include \"' + file_name.lower()+'\"\n'
            file_name3 = file_name3.replace('all_h','bit.h')
            file.write(file_name1)
            file.write(file_name2)
            #file.write(common_header)
            file.write(file_name3)
            sub_dir = sub_dir.upper()
            str1 = 'typedef volatile struct _AAAAA_MODULE_SUBM_T\n{\n'
            str2 = str1.replace('AAAAA',sub_dir)
            file.write(str2)
            file.write('\n'.join(list_out)) 
            str1 = '\n}AAAAA_MODULE_SUBM_T;\n'
            str2 = 'typedef volatile struct _AAAAA_MODULE_GLOBAL_T\n{\n'
            str3 = '    HANDLE_MODULE_E    HANDLE;\n    SYNC_TIMESTAMP_T    TS;\n'
            str4 = '    AAAAA_MODULE_SUBM_T    AAAAA;\n}AAAAA_MODULE_GLOBAL_T;\n'
            str5 = '#endif\n'
            #str6 = str1+str2+str3+str4+str5  
            str6 = str1+str5            
            str6 = str6.replace('AAAAA',sub_dir)
            file.write(str6)
    except:
        print('file not exist or corupted')
        sys.exit()
 
def __file_read_process(file_all,sub_dir):
    demo_lines_out_all = []
    for file_name in file_all:      
        lines = __read_file_lines(file_name)
        demo_lines_out = __file_line_process(lines)
        demo_lines_out_all = demo_lines_out_all + demo_lines_out
    out_file_name = __get_output_file_name(sub_dir)
    __wirte_list_to_file(demo_lines_out_all,out_file_name,sub_dir)
    
    
def  get_struct_all(dir_name,sub_dir):
    file_list = __get_input_file_name(dir_name,sub_dir)
    __mkdir_out_filefolder()     
    __file_read_process(file_list,sub_dir)
                          
def main(argv=None):
    if argv is None:
        argv = sys.argv
        if len(argv) < 2:
            print('please set argv as log file')
        else:                                           
            get_struct_all(argv[1],'uss')            
            print('generate file end');            

if __name__ == "__main__":
    sys.exit(main())
 