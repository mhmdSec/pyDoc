import pypdf 
import os

while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print('''
                    $$$$$$$\                      
                    $$  __$$\                     
 $$$$$$\  $$\   $$\ $$ |  $$ | $$$$$$\   $$$$$$$\ 
$$  __$$\ $$ |  $$ |$$ |  $$ |$$  __$$\ $$  _____|
$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /      
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      
$$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$  |\$$$$$$$\ 
$$  ____/  \____$$ |\_______/  \______/  \_______|
$$ |      $$\   $$ |                              
$$ |      \$$$$$$  |                              
\__|       \______/                               

    ''')
    print('-' * 15)
    print('1-Merging.\n2-Splitting.\n3-Encryption or Decryption.\n4-Extracting Text.')
    process = input("> ")
    print('-' * 15)

    if process == "1":
        print("Please add the path of the PDF files")
        file1 = input("First PDF path > ")
        file2 = input("Second PDF Path > ")
        files = [file1,file2]
        merger = pypdf.PdfWriter()
        for file in files :
            merger.append(file)
        merger.write('merged_copy.pdf')
        print('-'*15)
        print(f"{file1} and {file2} have successfully merged together.")
        merger.close()
        

    elif process == "2":
        print("Please add the path of the PDF file")
        
        file1 = input("Path > ")
        first_page = input("Please add the Start page number: ")
        last_page = input("Please add the End page number: ")
        
        splitter = pypdf.PdfWriter()
        splitter.append(file1,pages=pypdf.PageRange(f'{int(first_page)-1}:{int(last_page)}'))
        splitter.write("splitted_copy.pdf")
        print('-'*15)
        print(f"{file1} has successfully splitted from page {first_page} to page {last_page} !")
        splitter.close()

    elif process == "3":
        
        print("Encryption : 1\nDecryption : 2")
        sub_process = input("> ")
        
        print("Please add the path of PDF copy")
        file1 = input("Path > ")

        password = input("Please write the Encryption/Decryption password: ")
        
        reader = pypdf.PdfReader(file1)
        writer = pypdf.PdfWriter()
        
        if sub_process == "1":
                
            for page in reader.pages:
                writer.add_page(page)
            
            writer.encrypt(password)
            writer.write('Encrypted_copy.pdf')
            print('-'*15)
            print(f"File has encrypted by the password: {password}")
            writer.close()
            
            
        elif sub_process == "2":
            if reader.is_encrypted:
                reader.decrypt(password)

            for page in reader.pages:
                writer.add_page(page)

            writer.write('Decrypted_copy.pdf')
            print('-'*15)
            print(f"file has successfully decrypted!")
            writer.close()
            

    elif process == "4":
        
        print("Please add the path of the PDF File")
        file = input("> ")
        
        page_number = input("Please add the Page number > ")
        reader = pypdf.PdfReader(file)
        page = reader.pages[int(page_number)]
        
        print(page.extract_text())

    else:
        print("Please add a Valid Number !")
        continue
    break