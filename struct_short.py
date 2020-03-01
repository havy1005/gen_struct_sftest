#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import os
align_four = 0
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
        
def __file_line_process_submodule(line):
    try:
        mstr = line.split('\"')[1]
        Obj = re.compile( r'\[.*\]', re.I)
        if Obj :
            list1 = Obj.findall(mstr)
            if list1 !=[]:
                str1 =list1[0]
                str1 =str1.replace('[','')
                str1 =str1.replace(']','')
                dec1 = int(str1)
                return dec1
            else :
                dec1 = 0
                return dec1
    except:
        print('len of line is 1111 ')
        sys.exit() 
        
def __file_line_process_submodule_name(line):
    try:
        mstr = line.split('\"')[1]
        mstr = mstr.split('[')[0]
        return mstr
    except:
        print('len of line is 1111 ')
        sys.exit() 

def __demo_file_line_process_short(line,subm):
    out = '' 
    modulestr = line.split(' ')
    modulestr = modulestr[0]
    modulestr = modulestr.lower()
    try:
        out = '    sint16    ' + subm + '_' + modulestr
        global align_four
        align_four = align_four + 1
    except:
        print('len of line is 1 ')
        sys.exit() 
    return out  

def __get_output_file_name(out_file_name):
    try:       
        out_file_name = out_file_name.lower()
        out_file_name = 'out_dir\\tst_' + out_file_name + '_'+ 'struct_interface.h'    
        return out_file_name     
    except:
        print('len of line is 1 ')
        sys.exit() 
             
def __file_line_process(lines,subm): 
    lines_list=[]
    try: 
        for line in lines[2:]: 
            line_check = line[0:1]             
            if line_check !='' and line_check !='\n' and line_check !=' ' :         
                line_out = __demo_file_line_process_short(line,subm)
                line_out = line_out + ';'
                lines_list.append(line_out)                
        return lines_list     
    except:
        print('len of line is 22 ')
        sys.exit()

def __file_line_process_channel(lines,cnt,subm): 
    lines_list=[]
    try: 
        for line in lines[2:]: 
            line_check = line[0:1]             
            if line_check !='' and line_check !='\n' and line_check !=' ' :         
                line_out = __demo_file_line_process_short(line,subm)
                line_out = line_out + str(cnt) + ';'
                lines_list.append(line_out)                
        return lines_list     
    except:
        print('len of line is 22 ')
        sys.exit()
         
def __wirte_list_to_file(list_out,file_name):
    try:
        with open(file_name, 'w+') as file:
            file_name = file_name.split('\\')
            file_name = file_name[-1]
            file_name = file_name.replace('.','_')
            file_name1 = '#ifndef ' + file_name.upper()+'\n'
            file_name2 = '#define ' + file_name.upper()+'\n'
            common_header = '#include \"common_tst_struct_interface.h\"\n'
            file.write(file_name1)
            file.write(file_name2)
            file.write(common_header)
            file.write('\n'.join(list_out)) 
            file.write('\n#endif\n')
    except:
        print('file not exist or corupted')
        sys.exit()
 
def __file_read_process(file_all,sub_dir):
    lines_out_all = []
    sub_dir1 = sub_dir.lower()
    str1 = 'typedef struct _sftst_' + sub_dir1 + '_t\n{\n    sint32    enable;\n    SFTST_HANDLE_E    handle;' 
    lines_out_all.append(str1)
    global align_four
    align_four = 0
    for file_name in file_all:      
        lines = __read_file_lines(file_name)
        cnt1 = __file_line_process_submodule(lines[1])
        subm_name = __file_line_process_submodule_name(lines[1])
        print(subm_name)
        if cnt1 == 0:
            lines_out = __file_line_process(lines,subm_name)
            lines_out_all = lines_out_all + lines_out
        else :
            counter1 = 0
            while cnt1:
            #for index in range(cnt1)
                lines_out = __file_line_process_channel(lines,counter1,subm_name)
                counter1 = counter1 + 1
                cnt1 = cnt1 - 1
                lines_out_all = lines_out_all + lines_out
    if align_four & 1 :
         lines_out_all.append('    sint16    align_four_byte_unused;')
         #print(align_four)
    out_file_name = __get_output_file_name(sub_dir)
    str1 = '}sftst_AAAAA_t;\nextern    sftst_AAAAA_t    sftst_AAAAA_module;'
    str1 = str1.replace('AAAAA',sub_dir1)
    lines_out_all.append(str1)
    __wirte_list_to_file(lines_out_all,out_file_name)
    
    
def  get_struct_short(dir_name,sub_dir):
    file_list = __get_input_file_name(dir_name,sub_dir)
    __mkdir_out_filefolder()     
    __file_read_process(file_list,sub_dir)
                          
def main(argv=None):
    if argv is None:
        argv = sys.argv
        if len(argv) < 2:
            print('please set argv as log file')
        else:                                           
            get_struct_short(argv[1])            
            print('generate file end');            

if __name__ == "__main__":
    sys.exit(main())
 