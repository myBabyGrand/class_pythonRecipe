import os


#os.system('gdrive files mkdir GDRIVE')#폴더 생성

folderId = '' #folder Id는 생성 후 확인가능
fileName = input("FileName? : ")
deleteYn = input("after uploading, delete file y/n : ")

#upload and delete --> 지원안함
uploadCommand = "gdrive files upload --parent {0} {1}".format(folderId,fileName)

if deleteYn == 'Y' or deleteYn == 'y':
    try:
        os.system( uploadCommand )
        os.remove(fileName)
    except:
        print('gdrive file upload fail')
else:
    try:
        os.system( uploadCommand )
    except:
        print('gdrive file upload fail')


