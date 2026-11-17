# Lab 09 - Mạng nơ-ron nhiều lớp (MLP)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)


* **Họ và tên:** Huỳnh Hữu Phúc
* **MSSV:** 2474802010314
* **Môn:** Học Máy Và Ứng Dụng
* **LHP:** 261_71ITAI41203_0101
* **GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))

## Cấu trúc thư mục

```text
09_MLP/
├── README.md
├── requirements.txt
├── code/
│   ├── Lab09_5buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab09_BaiTap.ipynb
├── data/
│   ├── xor.csv
│   ├── hai_vang_trang.csv
│   ├── sinh_vien_mo_rong.csv
│   └── gia_nha.csv
├── figures/
│   └── toc_do_hoc.png
├── outputs/
│   ├── Lab09_5buoc_HuynhHuuPhuc_2474802010314.txt
│   └── Lab09_BaiTap.txt
└── scripts/
    └── run_all.py
```

## Dữ liệu và cách chia

| Nguồn | Nội dung và cách dùng |
|---|---|
| `data/xor.csv` | 400 điểm hai chiều, gồm 210 nhãn 0 và 190 nhãn 1. Dùng ở Bước 2 và Bài 1. |
| `data/hai_vang_trang.csv` | 300 điểm, 150 điểm mỗi lớp. Dùng ở Bước 3 và Bài 3. |
| `data/sinh_vien_mo_rong.csv` | 120 sinh viên, gồm 71 qua môn và 49 rớt. Ba biến đầu vào là số giờ ôn, điểm giữa kỳ và chi tiêu. Dùng ở Bước 4. |
| `load_digits()` | 1.797 ảnh chữ số 8 × 8, tương ứng 64 đặc trưng đầu vào. Dùng ở Bước 5, Bài 4 và Bài 5. |
| `data/gia_nha.csv` | 60 căn nhà. Bài 6 dùng riêng `dien_tich` (m²) để dự đoán `gia` (tỷ đồng), cùng cách chia 80/20 và `random_state=42` ở bước đánh giá của Lab 1. |

Các phần phân loại chia tập học/kiểm tra theo tỷ lệ 75/25, phân tầng theo nhãn, với `random_state=17`. Bài 5 dò 12 cặp tham số bằng kiểm định chéo 5 phần trên tập học. `StandardScaler` nằm trong pipeline nên được fit trên phần học của từng fold.

## Cài đặt và chạy

Yêu cầu Python 3.11 trở lên. Trong terminal ở thư mục `09_MLP/`, chạy hai lệnh sau.

```powershell
python -m pip install -r requirements.txt
python scripts/run_all.py
```

Script xác định thư mục dự án từ vị trí file và dùng IPython của môi trường Python đang chạy. Hai notebook có không gian biến riêng. Script lưu kết quả vào notebook và ghi hai nhật ký UTF-8 ở `outputs/`. Nếu một cell lỗi, script dừng và ghi thông tin lỗi vào nhật ký tương ứng. Bước 3 và Bài 5 huấn luyện nhiều mô hình qua kiểm định chéo nên thời gian chạy lâu hơn.

Bạn cũng có thể chạy từng notebook trực tiếp. Hãy đặt thư mục làm việc của kernel về `09_MLP/` để mã mẫu đọc đúng các đường dẫn `data/...`.

- **VS Code**. Mở `09_MLP/` làm workspace, đặt `jupyter.notebookFileRoot` thành `${workspaceFolder}`, chọn kernel vừa cài thư viện rồi bấm **Run All**.
- **Jupyter Notebook**. Chạy `python -m notebook` từ `09_MLP/`. Nếu `%pwd` ra thư mục `code/`, chạy `%cd ..` trong một cell tạm trước khi chạy các cell của bài.

Kết quả được kiểm tra trên Python 3.14.3 với các phiên bản trong `requirements.txt`. Số vòng và điểm số của MLP có thể thay đổi nhẹ theo phiên bản thư viện tối ưu và phép toán số.

## Kết quả 5 bước thực hành

| Bước | Kết quả chính |
|---|---|
| 1. Lan truyền tiến | Nơ-ron đơn cho `z=1.80`, sigmoid `0.8581`. Mạng đặt trọng số tay cho bảng XOR `[0, 1, 1, 0]`. |
| 2. MLP trên XOR | Logistic kiểm tra `0.4500`. MLP 1, 2, 4 và 8 nơ-ron ẩn lần lượt đạt `0.6900`, `0.6900`, `0.9300` và `0.9100`. |
| 3. Độ lớn mạng và điều chuẩn | Mạng `(100, 100)` với `alpha=1e-5` đạt `1.0000` học và `0.7467` kiểm tra. Kiểm định chéo chọn `alpha=1.0` với `0.8578` CV và `0.9067` kiểm tra. |
| 4. Chuẩn hoá | Accuracy kiểm tra từ `0.4000` trên dữ liệu thô lên `0.9000` sau chuẩn hoá. Mức đoán tất cả qua môn là `0.6000`. |
| 5. Chữ số viết tay | 7.510 tham số, 144 vòng, accuracy `0.9844`, sai 7/450 ảnh. Bật dừng sớm cho `0.9578`. SVM RBF đạt `0.9911`. |

Bước 3 giữ nguyên đoạn mẫu. Bảng sau ghi các giá trị trung gian chênh so với số in trong PDF.

| Số đo | PDF | Lần chạy này |
|---|---:|---:|
| Accuracy kiểm tra của mạng `(100, 100)`, alpha `1e-5` | 0.7333 | 0.7467 |
| Accuracy học của mạng `(100, 100)`, alpha `1.0` | 0.8800 | 0.8844 |
| Accuracy CV tại alpha `0.001` | 0.7733 | 0.7689 |
| Accuracy CV tại alpha `0.1` | 0.7644 | 0.7689 |

## Kết quả 6 bài tập

| Bài | Kết quả chính |
|---|---|
| 1. Tính bằng trọng số đã học | Xác suất NumPy và `predict_proba` khớp trên năm điểm XOR. Sai khác tuyệt đối lớn nhất khoảng `2.776e-17`. Notebook theo dõi từng lớp và giải thích kích thước ma trận. |
| 2. Mạng XOR khác | Hai ReLU giữ phần dương của hai hiệu đối dấu. Cộng lại cho trị tuyệt đối của hiệu, bằng XOR trên bốn đầu vào nhị phân. |
| 3. Hàm kích hoạt | Tanh và ReLU cùng đạt accuracy kiểm tra cao nhất `0.9067`. Logistic đạt `0.8533`. |
| 4. Tốc độ học | `0.0001` cho accuracy kiểm tra cao nhất `0.9889` sau 582 vòng. `0.1` dao động và đạt `0.9489`. [Xem bốn đường mất mát](figures/toc_do_hoc.png). |
| 5. Dò lưới | Cặp được chọn là (50,), alpha 1, accuracy CV 0.9785. Accuracy kiểm tra MLP 0.9822, SVM RBF 0.9911. MLP thấp hơn SVM 0,89 điểm phần trăm. |
| 6. Hồi quy giá nhà | MAE của tuyến tính là `0.2578` tỷ, của MLP là `0.5008` tỷ. Giá dự đoán cho 250 m² lần lượt là `19.9139` và `28.1758` tỷ. Diện tích này ngoài phạm vi dữ liệu, vốn chỉ đến 117,5 m². |
