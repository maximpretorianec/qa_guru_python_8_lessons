from zipfile import ZipFile


def test_check_exist_files_at_zip(zip_file_func):
    with ZipFile(zip_file_func['curr_zip_path'], "r") as myzip:
        name_list = myzip.namelist()
        assert zip_file_func['xls_file'] in name_list
        assert zip_file_func['xlsx_file'] in name_list
        assert zip_file_func['pdf_file'] in name_list


def test_check_xls_file_by_size(zip_file_func):
    with ZipFile(zip_file_func['curr_zip_path'], "r") as myzip:
        assert myzip.getinfo(zip_file_func['xls_file']).file_size == zip_file_func['xls_file_size']


def test_check_xlsx_file_by_size(zip_file_func):
    with ZipFile(zip_file_func['curr_zip_path'], "r") as myzip:
        assert myzip.getinfo(zip_file_func['xlsx_file']).file_size == zip_file_func['xlsx_file_size']


def test_check_pdf_file_by_size(zip_file_func):
    with ZipFile(zip_file_func['curr_zip_path'], "r") as myzip:
        assert myzip.getinfo(zip_file_func['pdf_file']).file_size == zip_file_func['pdf_file_size']
