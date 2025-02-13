# Tổng quan

## doitennhanh-hackerrank
**Version: 0.1**

Chương trình này được viết bởi **nguyenminhkhoi.io.vn**. Mục đích của chương trình là đổi tên các file `.inp` và `.out` trong thư mục nguồn và các thư mục con của nó, sau đó đóng gói các file đã đổi tên vào file zip `TEST.zip`.

**Lưu ý:** Chương trình mới chỉ được thử nghiệm trên Windows 11.

## Chức năng chính

### 1. Liệt kê các file trong thư mục gốc
- Duyệt qua tất cả các thư mục con và các file trong thư mục nguồn.
- In ra danh sách các file tìm thấy.

### 2. Đổi tên và di chuyển các file .inp và .out vào các thư mục input và output
- Tạo ba thư mục mới: `input`, `output` và `temp` nếu chúng chưa tồn tại.
- Đổi tên file `.inp` thành `input{stt}.txt` và di chuyển vào thư mục `input`.
- Đổi tên file `.out` thành `output{stt}.txt` và di chuyển vào thư mục `output`.
- Sao chép các file vào thư mục tạm trước khi đổi tên và di chuyển.

### 3. Đóng gói các file đã đổi tên vào file zip TEST.zip
- Tạo một file zip tên là `TEST.zip` chứa tất cả các file từ hai thư mục `input` và `output`.

### 4. Xóa các thư mục tạm sau khi đóng gói
- Xóa ba thư mục `input`, `output` và `temp` để làm sạch dữ liệu sau khi đóng gói.

## Hướng dẫn sử dụng

1. Chạy chương trình từ thư mục gốc chứa file `index.py`.
2. Nếu file `TEST.zip` đã tồn tại, chọn một trong các tùy chọn sau:
    - Đổi tên file `TEST.zip` hiện tại.
    - Xóa file `TEST.zip` hiện tại.
    - Hủy quá trình và thoát chương trình.
3. Chương trình sẽ tự động thực hiện các bước:
    - Liệt kê file.
    - Đổi tên và di chuyển file.
    - Đóng gói các file thành file zip.
    - Xóa các thư mục tạm.

## Chú thích

- Thư viện `os`: Dùng để tương tác với hệ điều hành.
- Thư viện `pathlib`: Dùng để xử lý đường dẫn.
- Thư viện `shutil`: Dùng để sao chép và di chuyển file.
- Thư viện `zipfile`: Dùng để tạo và xử lý file zip.
