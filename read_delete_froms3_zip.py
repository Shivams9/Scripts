import os
import zipfile

folder ='F:/zips'   #change location
text ='client_1166'
Available_count =0
NA_c=0

for file in os.listdir(folder):
    if file.endswith('.zip'):
        zip_path = os.path.join(folder,file)
        # print(f'filename--{file}')
        found = False

        with zipfile.ZipFile(zip_path,'r') as zip_file:
            
            for name in zip_file.namelist():

                with zip_file.open(name) as f:
                    content =f.read().decode('utf-8',errors='ignore')
                    # content = f.read().decode('utf-8', errors='ignore')
                    if text in content:
                        Available_count+=1
                        print(Available_count)
                        # print(f'found in  -- {file}')
                        found =True
                        break
        if not found:
                NA_c+=1
                print(f'Not found --{file}--deleting..')
                os.remove(zip_path)
                    
                                        
print(f'\nCount of total zip--{Available_count+NA_c}')
print(f'\nCount of Available total zip"{text}":{Available_count}')
print(f'\nCount of not available"{text}":{NA_c}')

