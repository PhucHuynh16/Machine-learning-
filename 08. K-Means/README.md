# Lab 08 - Phân cụm K-Means
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)


* **Họ và tên:** Huỳnh Hữu Phúc
* **MSSV:** 2474802010314
* **Môn:** Học Máy Và Ứng Dụng
* **LHP:** 261_71ITAI41203_0101
* **GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))

## Cấu trúc thư mục

```text
08. K-Means/
├── README.md
├── requirements.txt
├── code/
│   ├── Lab08_5buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab08_BaiTap.ipynb
├── data/
│   ├── khach_hang.csv
│   └── hai_vang_trang.csv
├── figures/
│   ├── silhouette_khach_hang.png
│   ├── anh_goc.png
│   ├── anh_16_mau.png
│   ├── anh_hoa_goc.png
│   └── anh_hoa_16_mau.png
├── outputs/
│   ├── Lab08_5buoc_HuynhHuuPhuc_2474802010314.txt
│   └── Lab08_BaiTap.txt
└── scripts/
    └── run_all.py
```

## Dữ liệu

| Nguồn | Nội dung và cách dùng |
|---|---|
| `data/khach_hang.csv` | 210 khách hàng mô phỏng với tuổi, thu nhập (triệu đồng/tháng) và điểm chi tiêu. Bước 2–4 và Bài 1–3 dùng bộ này. |
| `data/hai_vang_trang.csv` | 300 điểm, mỗi vầng trăng có 150 điểm. Mô hình chỉ học từ `x1`, `x2`. Cột `nhan` dùng để đánh giá sau khi phân cụm. |
| `china.jpg` và `flower.jpg` | Ảnh RGB của scikit-learn, kích thước 427 × 640. Ảnh hoa là ảnh thứ hai đã chọn cho Bài 4. |
| `load_digits()` | 1.797 ảnh chữ số 8 × 8. Bài 6 phân cụm theo 64 độ sáng pixel. Nhãn thật dùng để lập bảng chéo. |

Hai CSV trong `data/` khớp từng byte với bản trong ZIP Lab 8.

## Cài đặt và chạy

Yêu cầu Python 3.11 trở lên. Mở terminal ở thư mục `08. K-Means/` rồi chạy:

```powershell
python -m pip install -r requirements.txt
python scripts/run_all.py
```

Script tìm thư mục gốc theo vị trí của nó, dùng IPython của chính Python đang chạy script và đặt lại không gian biến giữa hai notebook. Script lưu kết quả vào notebook sau khi chạy xong từng file và ghi kết quả dạng chữ ở `outputs/`. Bài 1 và Bài 4 hiển thị hình trong notebook và lưu file PNG ở `figures/`. Khi có lỗi, script dừng và ghi thông tin lỗi vào nhật ký của notebook đang chạy.

Bạn cũng có thể chọn **Run All** trong VS Code hoặc Jupyter. Thư mục làm việc của kernel cần là `08. K-Means/` để các đường dẫn `data/...` trong mã gốc tìm được CSV.

- **VS Code**. Mở `08. K-Means/` làm workspace, đặt `jupyter.notebookFileRoot` thành `${workspaceFolder}` trong Workspace Settings rồi chọn kernel Python đã cài thư viện.
- **Jupyter Notebook**. Chạy `python -m notebook` trong `08. K-Means/`. Nếu `%pwd` cho biết kernel đang ở `code/`, chạy `%cd ..` trong một cell tạm trước khi chạy mã của bài.

Kết quả đã được kiểm tra bằng Python 3.14.3. Dung lượng PNG được lấy từ file thực tế và có thể thay đổi theo phiên bản bộ mã hoá ảnh.

## Kết quả 5 bước thực hành

| Bước | Kết quả chính |
|---|---|
| 1. Tự viết K-Means | Hội tụ sau 3 vòng. Hai cụm là A–B và C–G. Inertia tính tay và scikit-learn cùng bằng `8.5250`. |
| 2. Phân khúc khách hàng | Inertia `23.02`. Cụm 2 đông nhất (60 khách). Hai khách mới `(29, 85)` và `(9, 75)` lần lượt vào cụm 4 và 0. |
| 3. Chọn số cụm | Khuỷu tay và silhouette đều chọn `K=5`. Silhouette `0.723`, mức giảm inertia từ 4 lên 5 là `50.7`, từ 5 lên 6 là `2.1`. |
| 4. Ba cái bẫy | Khi bỏ chuẩn hoá, đổi thang thu nhập làm các nhóm tách chủ yếu theo thu nhập. 10/20 lần khởi tạo ngẫu nhiên đạt inertia `23.0`. K-Means khớp `0.7500` trên hai vầng trăng sau khi căn nhãn. |
| 5. Nén màu ảnh | Ảnh có 273.280 pixel và 96.615 màu. Bảng màu 4, 16 và 64 màu có sai lệch trung bình lần lượt `17.41`, `7.97` và `4.54` mức trên thang 255. |

## Kết quả 6 bài tập

| Bài | Kết quả chính |
|---|---|
| 1. Tự tính silhouette | Điểm trung bình tự tính và thư viện cùng bằng `0.722706`. Dòng 113 (chỉ số từ 0), cụm 2, có `s=0.028571`. Notebook giải thích cách tính cả `a`, `b` và đánh dấu khách trên hình. |
| 2. Thêm tuổi | `K=5` vẫn tốt nhất với silhouette `0.4808`. Bảng tâm cụm và bảng chéo cho thấy 5 khách đổi nhóm khi đối chiếu theo nhóm có thành viên tương ứng. |
| 3. So sánh khởi tạo | Random đạt inertia `23.0` ở 30/50 lượt và K-Means++ đạt ở 50/50 lượt, theo giá trị làm tròn một chữ số thập phân. Notebook giải thích vì sao cách chọn tâm ban đầu ảnh hưởng nghiệm cuối. |
| 4. Lưu ảnh 16 màu | China giảm từ 550.154 xuống 134.509 byte (4,09 lần). Ảnh hoa giảm từ 419.413 xuống 55.634 byte (7,54 lần). Hai cặp được lưu dưới dạng PNG. |
| 5. DBSCAN | `eps=0.2, 0.3, 0.4` đều cho 1 cụm, với 40, 10 và 3 điểm nhiễu. Cả ba gộp hai vầng trăng trên dữ liệu này. |
| 6. Phân cụm chữ số | Số 0 tập trung rõ nhất (176/178 vào một cụm). Cụm 1 trộn 100 ảnh số 1 và 100 ảnh số 8. Cụm 8 có nhiều ảnh số 9, 8 và 5. |

## Dùng ảnh riêng trong Bài 4

1. Đặt ảnh PNG hoặc JPG vào `data/`, ví dụ `data/anh_cua_minh.png`.
2. Trong cell Bài 4, đổi `duong_dan_anh_rieng = None` thành `duong_dan_anh_rieng = Path("data/anh_cua_minh.png")` rồi chạy lại. Ảnh được đọc bằng `plt.imread`. Với PNG RGBA, cell lấy ba kênh RGB.
3. So sánh `figures/anh_rieng_goc.png` và `figures/anh_rieng_16_mau.png`. Kết quả in ngay dưới cell, hoặc trong nhật ký Bài tập khi chạy qua script.
