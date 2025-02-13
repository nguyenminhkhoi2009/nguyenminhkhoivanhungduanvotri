# Code bởi nguyenminhkhoi.io.vn
# Version: 0.1
# Phục vụ cho Hackerrank
# Chương trình đổi tên các file .inp và .out, sau đó đóng gói chúng vào file zip TEST.zip
# Chức năng chính:
# 1. Liệt kê các file trong thư mục gốc
# 2. Đổi tên và di chuyển các file .inp và .out vào các thư mục input và output
# 3. Đóng gói các file đã đổi tên vào file zip TEST.zip
# 4. Xóa các thư mục tạm sau khi đóng gói

import os  # Thư viện os dùng để tương tác với hệ điều hành
from pathlib import Path  # Thư viện pathlib dùng để xử lý đường dẫn
import shutil  # Thư viện shutil dùng để sao chép và di chuyển file
import zipfile  # Thư viện zipfile dùng để tạo và xử lý file zip

def list_files(src_directory):
    """
    Liệt kê tất cả các file trong thư mục gốc và các thư mục con của nó
    """
    src_path = Path(src_directory)
    print(f"Duyệt qua thư mục: {src_path}")

    # Duyệt qua các thư mục con và các file
    for subdir, dirs, files in os.walk(src_path):
        subdir_path = Path(subdir)
        print(f"Duyệt qua thư mục con: {subdir_path}")
        for file in files:
            file_path = subdir_path / file
            print(f"Tìm thấy file: {file_path}")

def rename_and_move_files(src_directory):
    """
    Đổi tên và di chuyển các file .inp và .out vào các thư mục input và output
    """
    src_path = Path(src_directory)

    # Tạo các thư mục đích nếu chưa tồn tại
    input_dir = src_path / 'input'
    output_dir = src_path / 'output'
    temp_dir = src_path / 'temp'
    input_dir.mkdir(exist_ok=True, parents=True)
    output_dir.mkdir(exist_ok=True, parents=True)
    temp_dir.mkdir(exist_ok=True, parents=True)
    print(f"Tạo các thư mục input, output và temp")

    # Khởi tạo số thứ tự bắt đầu từ 0
    stt = 0

    # Duyệt qua các thư mục con và các file
    for subdir, dirs, files in os.walk(src_path):
        subdir_path = Path(subdir)
        print(f"Duyệt qua thư mục con: {subdir_path}")

        # Kiểm tra xem thư mục có chứa các file .inp và .out không
        inp_files = [file for file in files if file.lower().endswith('.inp')]
        out_files = [file for file in files if file.lower().endswith('.out')]
        
        if inp_files or out_files:
            for file in inp_files:
                file_path = subdir_path / file
                temp_file_path = temp_dir / file
                shutil.copy(file_path, temp_file_path)  # Sao chép file vào thư mục tạm
                new_name = f'input{stt}.txt'
                shutil.move(temp_file_path, input_dir / new_name)  # Đổi tên và di chuyển file vào thư mục input
                print(f"Đã đổi tên {file_path} thành {input_dir / new_name}")

            for file in out_files:
                file_path = subdir_path / file
                temp_file_path = temp_dir / file
                shutil.copy(file_path, temp_file_path)  # Sao chép file vào thư mục tạm
                new_name = f'output{stt}.txt'
                shutil.move(temp_file_path, output_dir / new_name)  # Đổi tên và di chuyển file vào thư mục output
                print(f"Đã đổi tên {file_path} thành {output_dir / new_name}")

            # Tăng số thứ tự lên 1 sau khi xử lý xong các file trong một thư mục con
            stt += 1
            print(f"Số thứ tự hiện tại: {stt}")

def create_zip(src_directory):
    """
    Tạo file zip từ hai thư mục input và output
    """
    src_path = Path(src_directory)
    input_dir = src_path / 'input'
    output_dir = src_path / 'output'

    # Tạo file zip từ thư mục input và output
    with zipfile.ZipFile(src_path / 'TEST.zip', 'w') as zipf:
        for folder in [input_dir, output_dir]:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = Path(root) / file
                    zipf.write(file_path, file_path.relative_to(src_path))  # Đóng gói file vào file zip
                    print(f"Đã thêm {file_path} vào TEST.zip")
    print(f"Đã tạo file TEST.zip")

def clean_up(src_directory):
    """
    Xóa các thư mục input, output và temp sau khi đóng gói
    """
    src_path = Path(src_directory)
    input_dir = src_path / 'input'
    output_dir = src_path / 'output'
    temp_dir = src_path / 'temp'

    # Xóa các thư mục input, output và temp
    shutil.rmtree(input_dir)
    shutil.rmtree(output_dir)
    shutil.rmtree(temp_dir)
    print(f"Đã xóa các thư mục input, output và temp")

def main():
    """
    Hàm chính điều khiển chương trình
    """
    # Đường dẫn tới thư mục gốc chứa file index.py
    src_directory = os.path.dirname(os.path.abspath(__file__))

    # Kiểm tra nếu file TEST.zip tồn tại
    test_zip = Path(src_directory) / 'TEST.zip'
    if test_zip.exists():
        print(f"File TEST.zip đã tồn tại. Vui lòng chọn một trong các tùy chọn sau:")
        print("1. Đổi tên file TEST.zip hiện tại")
        print("2. Xóa file TEST.zip hiện tại")
        print("3. Hủy quá trình và thoát chương trình")
        choice = input("Nhập lựa chọn của bạn (1, 2, hoặc 3): ")

        if choice == '1':
            new_name = input("Nhập tên mới cho file TEST.zip: ")
            new_zip = Path(src_directory) / new_name
            test_zip.rename(new_zip)  # Đổi tên file zip hiện tại
            print(f"Đã đổi tên file TEST.zip thành {new_zip}")
        elif choice == '2':
            test_zip.unlink()  # Xóa file zip hiện tại
            print("Đã xóa file TEST.zip")
        elif choice == '3':
            print("Đã hủy quá trình và thoát chương trình")
            return
        else:
            print("Lựa chọn không hợp lệ. Thoát chương trình.")
            return

    # Liệt kê các file trong thư mục
    list_files(src_directory)

    # Đổi tên và di chuyển các file
    rename_and_move_files(src_directory)

    # Đóng gói các file thành file zip
    create_zip(src_directory)

    # Xóa các thư mục sau khi đóng gói
    clean_up(src_directory)

if __name__ == "__main__":
    main()
