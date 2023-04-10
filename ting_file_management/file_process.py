from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    process_exist = False
    for process in range(len(instance._data)):
        data = instance.search(process)
        if data == path_file:
            process_exist = not process_exist
            break

    if not process_exist:
        instance.enqueue(path_file)
        file = txt_importer(path_file)
        file_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        return print(file_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
