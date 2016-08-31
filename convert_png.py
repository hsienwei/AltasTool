# coding=utf8

import os, glob, shutil 
import xml.etree.ElementTree as ET
#import tinify

TEXTURE_PACKER_EXE = ''
TARGET_DIR = ''
OUTPUT_DIR = ''
PNG_QUANT_EXE = ''
BLACK_LIST = ''
PNG_OPT_LIST = ''


def file_copy( root, files, target_dir):
    for f in files:
        fullpath = os.path.join(root, f)
        shutil.copy(fullpath, target_dir)

def build_blacklist( blacklist_path, target_list, rootpath ):
    if not os.path.exists( blacklist_path ):
        print 'blacklist not found : ' + blacklist_path
    else:
        with open( blacklist_path, "r") as f:
            for line in f:
                fullpath = os.path.join(rootpath, line.strip())
                if os.path.exists( fullpath ):
                    target_list.append(fullpath)
        print "blacklist count:" + str(len(target_list) )         

def convert_pngoptlist( pngoptlist_path, rootpath ):
    if not os.path.exists( PNG_QUANT_EXE ):
        print 'PNG_QUANT_EXE not found '
        return

    if not os.path.exists( pngoptlist_path ):
        print 'pngoptlist not found : ' + pngoptlist_path
    else:
        with open( pngoptlist_path, "r") as f:
            for line in f:
                fullpath = os.path.join(rootpath, line.strip())
                if os.path.exists( fullpath ):
                    print 'exist  !  convert it. ' + fullpath
                    args = ' --force --output ' + fullpath + ' --verbose 256 ' + ' -- '+ fullpath
                    os.system('"' + PNG_QUANT_EXE + '"' + args) 
      
                
def check_blacklist( target_path, blacklist ):
    for blacklist_path in blacklist:
        p1 = os.path.abspath(target_path)
        p2 = os.path.abspath(blacklist_path)
        if (p1 == p2):
            return True
    return False    

def convert( ):

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR) 
    
    black_list = []
    build_blacklist( BLACK_LIST , black_list, TARGET_DIR)   
    
           
    for root, dirs, files in os.walk(TARGET_DIR):
        
        '''
        建立對應資料夾
        '''
        for d in dirs:   
            fullpath = os.path.join(root, d)
            relpath =  os.path.relpath( fullpath, TARGET_DIR )
            print '========================================='
            print 'goto ' + fullpath  + "root :" + root +" rel: " + relpath
            fullpath2 = os.path.join(OUTPUT_DIR, relpath)
            if not os.path.exists(fullpath2):
                os.mkdir(fullpath2)   
                print 'create dir: '+ fullpath2
            
            '''
            copy相關檔案
            '''
            #print 'copy need files.'
            types = ( '*.plist', '*.png') # the tuple of file types
            files_grabbed = []
            for files in types:
                files_grabbed.extend(glob.iglob(os.path.join(fullpath, files)))
            file_copy( root, files_grabbed, fullpath2)
            
            '''
            png 轉 pvr.ccz
            '''
            files_grabbed = glob.iglob(os.path.join(fullpath2, '*.png'))
            for file in files_grabbed:
            
                '''
                確認是否為黑名單.
                '''
                check_rel_path = os.path.relpath(file, OUTPUT_DIR)
                checkpath = os.path.join(TARGET_DIR, check_rel_path)
                
                if  check_blacklist(checkpath, black_list ):
                    print 'in blacklist ,pass. ' + file
                    '''
                    args = ' --force --output ' + file + ' --verbose 256 ' + ' -- '+ file
                    os.system('"' + PNG_QUANT_EXE + '"' + args) 
                    '''
                    
                    continue
  
                
                '''
                確認plist存在.
                '''
                filename, file_extension = os.path.splitext(file)
                plist_name = filename + '.plist'
                #print '--'
                print 'check has .plist ' + plist_name
                if not os.path.exists( plist_name ):
                    print "plist :" + plist_name + ' not exist'
                    continue
                    
                '''
                確認是texture產出的plist.
                '''            
                tree = ET.parse(plist_name)
                xmlroot = tree.getroot()
                check = 0
                for element in xmlroot.findall("./dict/key"):
                    if element.text == 'frames':
                        check = check + 1
                    if element.text == 'metadata':
                        check = check + 1
                
                if not check == 2:
                    print 'not pass texture plist check.'
                    continue
                print 'png 2 pvr.ccz: ' + file 
                pvr_name = file.replace(".png", ".pvr.ccz")
                args = ' ' + file + ' --sheet ' + pvr_name  + ' --format cocos2d --opt RGBA4444 --dither-fs-alpha --size-constraints AnySize --allow-free-size --disable-rotation --trim-mode None --border-padding 0 --inner-padding 0'
                os.system('"' + TEXTURE_PACKER_EXE + '"' + args) 
                os.remove(file)   
    
    opt_list = []    
    convert_pngoptlist( PNG_OPT_LIST , OUTPUT_DIR)  



if __name__ == "__main__":
    TEXTURE_PACKER_EXE = 'C:\\Program Files (x86)\\CodeAndWeb\\TexturePacker\\bin\\TexturePacker.exe'
    TARGET_DIR = '..\\..\\Art\\animates'
    OUTPUT_DIR = '..\\..\\..\\4_Data\\Resources\\herogo\\animates' #'.\\output'
    PNG_QUANT_EXE = 'D:\\pngquant\\pngquant.exe'
    BLACK_LIST = ''
    PNG_OPT_LIST = ''
    
    convert( )
    print '\npress enter to end...'            
    raw_input()
