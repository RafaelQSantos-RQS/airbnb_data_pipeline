import os

def clean_path(path:str):
    '''
    '''
    print(f"Listando os arquivos do diretório {path}")
    files_list = [os.path.join(path,file) for file in os.listdir(path=path)]
    
    print(f"Será apagados {len(files_list)} arquivos.")
    for file_path in files_list:
        print(f"O arquivo {file_path} está sendo apagado.")
        os.remove(path=file_path)
        print(f"Arquivo {file_path} apagado com sucesso!!")