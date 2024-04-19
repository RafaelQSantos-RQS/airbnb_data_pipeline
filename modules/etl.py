import os
import gzip
import shutil
import requests
from concurrent.futures import ThreadPoolExecutor

class Landing:
    def __init__(self,landing_path:str) -> None:
        self.landing_path = landing_path

    def extract(self,url:list[str]):
        '''
        '''
        def get_data_and_download(url:str):
            '''
            '''
            try:
                print(f"Efetuando a requisição para a url {url}")
                response = requests.get(url=url,stream=True)
                response.raise_for_status()

                save_path = os.path.join(self.landing_path,url.split('/')[-1])
                print(f"Salvando o arquivo {save_path}")
                with open(save_path,'wb') as response_file:
                    response_file.write(response.content)
            except requests.RequestException as req:
                print(f"Erro ao efetuar a requisição na url {url}: {req}")
            except Exception as e:
                print(f"Erro inesperado ao efetuar a requisição na url {url}: {req}")

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(get_data_and_download,link) for link in url]
        
        for future in futures:
            future.result()

        

    def transform(self):
        '''
        '''
        landing_path = self.landing_path
        list_of_files = os.listdir(landing_path)

        # Extract files
        for file in list_of_files:
            file = os.path.join(landing_path,file)
            with gzip.open(file,'rb') as f_in:
                with open(file[:-3],'wb') as f_out:
                    shutil.copyfileobj(f_in,f_out)

        # Remove files
        for file in list_of_files:
            file = os.path.join(landing_path,file)
            os.remove(file)