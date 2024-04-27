import os
from datetime import datetime
import great_expectations as gx

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

def verifica_colunas_datetime(gx_df, colunas_datetime:list):
    '''
    '''
    for coluna in colunas_datetime:
        condicao_tipo = gx_df.expect_column_values_to_be_in_type_list(coluna,['datetime64[ns]']).get('success')
        condicao_data_valida = gx_df.expect_column_values_to_be_between(coluna,datetime(2008,8,1),datetime.now()).get('success')
        if (condicao_tipo) and (condicao_data_valida):
            print(f"A coluna '{coluna}' é válida. (Tipo e Valor)")
        else:
            if condicao_tipo == False:
                print(f"A coluna '{coluna}' não está no formato correto que é datetime.")
            if condicao_data_valida == False:
                print(f"A coluna '{coluna}' tem valores inválidos.")

def verificar_colunas_categoricas(gx_df,coluna_a_ser_analisada,valores_esperados):
    '''
    '''
    if gx_df.expect_column_values_to_be_in_set(coluna_a_ser_analisada,valores_esperados).get('success'):
        print(f"Os valores da coluna {coluna_a_ser_analisada}, só contém valores esperados. ({valores_esperados})")
    else:
        print(f"Os valores da coluna {coluna_a_ser_analisada}, só contém valores inesperados. ({valores_esperados})")

def verificar_colunas_booleanas(gx_df,list_of_columns:list):
    '''
    '''
    for column in list_of_columns:
        condicao_tipo = gx_df.expect_column_values_to_be_in_type_list(column,['int','int64']).get('success')
        condicao_dalor_valido = gx_df.expect_column_values_to_be_in_set(column,[1,0]).get('success')
        if condicao_tipo and condicao_dalor_valido:
                print(f"A coluna '{column}' é válida. (Tipo e Valor)")
        else:
            if condicao_tipo:
                print(f"A coluna '{column}' não está no formato correto que é datetime.")
            if condicao_dalor_valido:
                print(f"A coluna '{column}' tem valores inválidos.")

def verificar_collunas_com_none(gx_df,list_of_columns:list):
    '''
    '''
    for column in list_of_columns:
        condicao_valores_nulos = gx_df.expect_column_values_to_not_be_null(column)
        if condicao_valores_nulos:
            print(f"A coluna '{column}' é válida. (Não tem valores nulos)")
        else:
            print(f"A coluna '{column}' é válida. (Tem valores nulos)")