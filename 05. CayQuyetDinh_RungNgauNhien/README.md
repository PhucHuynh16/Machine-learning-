# Lab 05: Cây quyết định và Rừng ngẫu nhiên

- **Môn học:** Học máy và ứng dụng
- **Sinh viên:** Huỳnh Hữu Phúc
- **MSSV:** 2474802010314

## Nội dung

Bài làm theo bố cục Lab 3, gồm đúng **hai notebook**, có mã, kết quả thực thi và nhận xét bằng tiếng Việt:

1. `code/Lab05_7buoc_HuynhHuuPhuc_2474802010314.ipynb`: đủ 7 bước, dùng trực tiếp bảy đoạn code mẫu trong `Lab05_CayQuyetDinh_RungNgauNhien.pdf`. Chỉ bỏ số dòng, khôi phục thụt dòng và thay dấu trừ Unicode của bản trích PDF bằng dấu trừ Python. Giữ nguyên thuật toán, dữ liệu, tham số, thứ tự lệnh và nội dung in.
2. `code/Lab05_BaiTap.ipynb`: giải đủ 6 bài ở mục 9, mở rộng code mẫu theo đúng yêu cầu, kèm hai hình cây và nhận xét chi tiết.

Mỗi notebook có thêm một cell chuẩn bị đường dẫn, tách riêng khỏi các bước/bài tập. Không có file mã nguồn `.py` trong bài làm. PDF đề gốc nằm ở thư mục Lab 5 bên ngoài, không sao chép vào thư mục bài nộp.

## Cấu trúc

```text
05. CayQuyetDinh_RungNgauNhien/
├── README.md
├── requirements.txt
├── code/
│   ├── Lab05_7buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab05_BaiTap.ipynb
├── data/
│   ├── khach_vay.csv
│   └── gia_nha.csv
├── figures/
│   ├── cay_nam_la.png
│   └── cay_sau_2.png
├── scripts/
│   └── run_all.py 
└── outputs/
    ├── Lab05_7buoc_HuynhHuuPhuc_2474802010314.txt
    └── Lab05_BaiTap.txt
```

## Dữ liệu

Hai CSV được sao chép nguyên nội dung từ `Lab05_data/data/`, không sửa, không tạo dữ liệu thay thế:

| Dataset | Kích thước | Sử dụng |
|---|---|---|
| `khach_vay.csv` | 600 dòng, 5 cột | Bốn đặc trưng dự đoán `tra_dung_han`: 305 khách trễ hạn, 295 khách đúng hạn. |
| `gia_nha.csv` | 60 dòng, 4 cột | Chỉ dùng `dien_tich` dự đoán `gia`, theo đúng mẫu Lab 5. |

Cả hai không có ô thiếu hoặc dòng trùng. Thu nhập tính bằng triệu đồng/tháng, giá nhà tính bằng tỷ đồng, diện tích tính bằng m². Dữ liệu khách vay là dữ liệu mô phỏng phục vụ giảng dạy theo đề.

## Cài đặt và chạy

Khuyến nghị **Python 3.11**. Mở PowerShell tại thư mục `05. CayQuyetDinh_RungNgauNhien`, tạo môi trường riêng:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m notebook
```

Trong Jupyter, mở từng notebook ở `code/`, chọn kernel của môi trường vừa cài, rồi **Restart Kernel and Run All** và lưu notebook. Nếu Jupyter hiện nhiều kernel, đăng ký môi trường một lần:

```powershell
.\.venv\Scripts\python.exe -m ipykernel install --user --name lab05 --display-name "Python (Lab05)"
```

Cũng có thể mở bằng VS Code, chọn interpreter `.venv/Scripts/python.exe` và **Run All**. Cell chuẩn bị tự chuyển lên thư mục gốc nếu kernel bắt đầu ở `code/`; vì vậy các đoạn code mẫu vẫn dùng nguyên đường dẫn `data/...`.

Hai notebook chạy độc lập; nên chạy từ đầu đến cuối trong từng notebook. Kết quả đã được lưu sẵn, kể cả hai hình nhúng trong notebook bài tập. Chạy lại Bài 1 sẽ ghi lại hai PNG trong `figures/`.

Các file `.txt` là bản xuất văn bản từ lần chạy kiểm tra đã bàn giao, kèm nhận xét. Khi tự chạy lại, kết quả trong notebook và hai PNG được cập nhật; log `.txt` không tự ghi lại. Đề yêu cầu ảnh chụp màn hình kết quả: có thể chụp các output đã hiển thị trong notebook để bổ sung khi giảng viên yêu cầu; các PNG cây là hình xuất trực tiếp bằng `plt.savefig`.

## Bảy bước thực hành

| Bước | Nội dung | Kết quả chính |
|---|---|---|
| 1 | Tự tính Gini trên 10 khách | Gini gốc 0,4800; ngưỡng thu nhập 12,0; mức giảm 0,1633. |
| 2 | Cây năm lá và hai khách mới | Sâu 3; train 0,7978; test 0,7467; hai khách được dự đoán đúng hạn/trễ hạn. |
| 3 | Quá khớp và chọn độ sâu bằng CV | Cây tự do test 0,7667; chọn độ sâu 5, CV 0,8333, test 0,8533. |
| 4 | Kiểm chứng không cần chuẩn hoá | Ba cách đều test 0,8533; không có dự đoán khác nhau. |
| 5 | Rừng ngẫu nhiên | Rừng 200 cây test 0,9000; bootstrap có 286/450 khách khác nhau. |
| 6 | Độ quan trọng đặc trưng | Thu nhập 0,479; tỷ lệ nợ 0,339; cột nhiễu được 0,150 khi thêm vào, đứng thứ 3. |
| 7 | Cây hồi quy so với đường thẳng | MAE cây 0,5039 tỷ; đường thẳng 0,2578 tỷ; cây không ngoại suy xu hướng. |

Các kết quả chính của 7 bước khớp bảng kết quả trong PDF.

## Sáu bài tập

| Bài | Kết quả và kết luận |
|---|---|
| 1. Vẽ cây | Lưu đủ hai hình. Hai lá bên trái của cây sâu 2 đều là lớp 0, nhưng phép chia vẫn giảm Gini có trọng số khoảng 0,0540. |
| 2. Tự tìm câu hỏi gốc | `thu_nhap <= 15.05`; Gini giảm 0,122145 trên 450 khách train, trùng scikit-learn. |
| 3. Gini/entropy | Cả hai chọn độ sâu 5; test Gini 0,8533 và entropy 0,8467, chênh 1/150 mẫu. |
| 4. Số khách tối thiểu tại lá | Chọn `min_samples_leaf=10`, CV 0,8089, test 0,8467; cây sâu 5 đạt 0,8533, tốt hơn một chút. |
| 5. Permutation importance | Cột nhiễu từ hạng 3 theo MDI xuống hạng 5 theo permutation; trung bình 0,0017, độ lệch chuẩn 0,0111. |
| 6. Rừng hồi quy | MAE rừng 0,4559 tỷ, tốt hơn cây 0,5039 nhưng kém đường thẳng 0,2578; dự đoán 250 m² khoảng 9,1973 tỷ, không ngoại suy xu hướng. |

## Quy tắc tái lập kết quả

- Phân loại: test 25%, `random_state=17`, `stratify=y`, nên train/test là 450/150.
- Hồi quy: chỉ dùng diện tích, test 20%, `random_state=42`, nên train/test là 48/12.
- Cây/rừng: `random_state=0`; rừng chính dùng 200 cây; CV 5 phần giữ mặc định giống code mẫu.
- Chọn tham số bằng CV trên train; nếu điểm bằng nhau, giữ giá trị xuất hiện trước trong vòng lặp. Không chọn tham số bằng accuracy test. Bảng số cây theo test ở Bước 5 được giữ đúng mẫu để minh hoạ.
- Bài 5 dùng `default_rng(0)` tạo nhiễu train trước, sau đó lấy tiếp số từ cùng RNG cho test; permutation dùng 20 lần, `random_state=0`, `scoring="accuracy"`.
- MDI không chứng minh quan hệ nhân quả. Permutation đo mức giảm accuracy, không phải các tỷ trọng có tổng bằng 1. Ngưỡng 15,05 không bắt buộc là gốc của các cây trong rừng do bootstrap và chọn cột ngẫu nhiên.

Đã kiểm tra bằng Python 3.11.9, NumPy 2.4.6, pandas 3.0.6, SciPy 1.17.1, scikit-learn 1.5.2 và Matplotlib 3.11.0. `requirements.txt` cố định phiên bản scikit-learn đã dùng, các thư viện còn lại có khoảng phiên bản tương thích. Giá trị rất sát điểm làm tròn có thể khác chữ số cuối do số thực; số liệu MAE và accuracy ở trên lấy trực tiếp từ lần chạy thực tế.
