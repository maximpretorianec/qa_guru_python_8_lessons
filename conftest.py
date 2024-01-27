import os, shutil, pytest
from utils import TMP_PATH

@pytest.fixture
def zip_file_func():
    files_info = {"res_folder": 'resources', "destination_folder": 'tmp', "zip_file": 'res_files.zip',
                  "xls_file": 'file_example_XLS_10.xls', "xlsx_file": 'file_example_XLSX_50.xlsx',
                  "pdf_file": 'Python Testing with Pytest (Brian Okken).pdf'}

    files_info["xls_file_path"] = os.path.join(files_info["res_folder"], files_info["xls_file"])
    files_info["xlsx_file_path"] = os.path.join(files_info["res_folder"], files_info["xlsx_file"])
    files_info["pdf_file_path"] = os.path.join(files_info["res_folder"], files_info["pdf_file"])
    files_info["xls_file_size"] = os.path.getsize(files_info["xls_file_path"])
    files_info["xlsx_file_size"] = os.path.getsize(files_info["xlsx_file_path"])
    files_info["pdf_file_size"] = os.path.getsize(files_info["pdf_file_path"])
    shutil.make_archive(files_info["zip_file"].split(".")[0], "zip", files_info["res_folder"])

    if not os.path.exists(TMP_PATH):
        os.mkdir(files_info["destination_folder"])

    new_location = shutil.move(os.path.join(os.path.curdir, files_info["zip_file"]), files_info["destination_folder"])
    print("% s перемещен в указанное место, % s" % (files_info["zip_file"], new_location))
    files_info["curr_zip_path"] = os.path.join(files_info["destination_folder"], files_info["zip_file"])

    yield files_info

    os.remove(os.path.join(files_info["destination_folder"], files_info["zip_file"]))
