# Tổng quan
doitennhanh-hackerrank
**Version: 0.1**

Chương trình này được viết bởi **nguyenminhkhoi.io.vn**. Mục đích của chương trình là đổi tên các file `.inp` và `.out` trong thư mục nguồn và các thư mục con của nó, sau đó đóng gói các file đã đổi tên vào file zip `TEST.zip`.
Để chạy chương trình thì bạn hãy cài đặt python cùng với các thư viện cần thiết (ở phần chú thích), bạn có thể chạy chương trình thông qua 2 cách là mở file trực tiếp hoặc chạy qua terminal.
**Lưu ý:** chương trình mới chỉ được thử nghiệm trên Windows 11.

## Chức năng chính

1. **Liệt kê các file trong thư mục gốc**
    - Chức năng này sẽ duyệt qua tất cả các thư mục con và các file trong thư mục nguồn và in ra danh sách các file tìm thấy.

2. **Đổi tên và di chuyển các file .inp và .out vào các thư mục input và output**
    - Chương trình sẽ tạo ba thư mục mới: `input`, `output` và `temp` nếu chúng chưa tồn tại.
    - Các file `.inp` sẽ được đổi tên thành `input{stt}.txt` và di chuyển vào thư mục `input`.
    - Các file `.out` sẽ được đổi tên thành `output{stt}.txt` và di chuyển vào thư mục `output`.
    - Các file sẽ được sao chép vào thư mục tạm trước khi đổi tên và di chuyển.

3. **Đóng gói các file đã đổi tên vào file zip TEST.zip**
    - Chương trình sẽ tạo một file zip tên là `TEST.zip` chứa tất cả các file từ hai thư mục `input` và `output`.

4. **Xóa các thư mục tạm sau khi đóng gói**
    - Sau khi đóng gói các file vào file zip, chương trình sẽ xóa ba thư mục `input`, `output` và `temp` để làm sạch dữ liệu.

## Hướng dẫn sử dụng

- Chạy chương trình từ thư mục gốc chứa file `index.py`.
- Nếu file `TEST.zip` đã tồn tại, chương trình sẽ yêu cầu người dùng chọn một trong các tùy chọn sau:
    1. Đổi tên file `TEST.zip` hiện tại
    2. Xóa file `TEST.zip` hiện tại
    3. Hủy quá trình và thoát chương trình

- Chương trình sẽ tự động thực hiện các bước liệt kê file, đổi tên và di chuyển file, đóng gói các file thành file zip, và cuối cùng là xóa các thư mục tạm.

## Chú thích

- Thư viện `os`: Dùng để tương tác với hệ điều hành.
- Thư viện `pathlib`: Dùng để xử lý đường dẫn.
- Thư viện `shutil`: Dùng để sao chép và di chuyển file.
- Thư viện `zipfile`: Dùng để tạo và xử lý file zip.
