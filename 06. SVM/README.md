# Lab 06 - Máy vectơ hỗ trợ (SVM)

- **Môn học** Học máy ứng dụng
- **Sinh viên** Huỳnh Hữu Phúc
- **MSSV** 2474802010314

## Nội dung

1. `Lab06_5buoc_HuynhHuuPhuc_2474802010314.ipynb` gồm năm bước thực hành ở các mục 2–6 của `Lab06_SVM.pdf`. Mỗi bước giữ nguyên đoạn mã mẫu và có nhận xét sau kết quả.
2. `Lab06_BaiTap.ipynb` giải sáu bài tập ở mục 7. Mỗi bài có đề, mã, kết quả đã chạy và nhận xét.

## Cấu trúc thư mục

```text
06. SVM/
│
├── README.md
├── requirements.txt
│
├── code/
│   ├── Lab06_5buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab06_BaiTap.ipynb
│
├── data/
│   ├── sinh_vien.csv
│   │   # 120 mẫu: 49 rớt, 71 qua môn
│   ├── sinh_vien_mo_rong.csv
│   │   # 120 mẫu, thêm cột chi_tieu
│   └── hai_vang_trang.csv
│       # 300 mẫu, 150 mẫu mỗi lớp
│
├── figures/
│   # 4 ảnh dự đoán sai
│   # 1 ảnh tổng hợp ở Bài 5
│
├── outputs/
│   ├── Lab06_5buoc_HuynhHuuPhuc_247480201...
│   │   # File kết quả TXT
│   └── Lab06_BaiTap.txt
│       # File kết quả bài tập
│
└── scripts/
    └── run_all.py
        # Script chạy chương trình
```

Bộ chữ số viết tay được nạp bằng `load_digits()` từ scikit-learn. Đề gốc `Lab06_SVM.pdf` được cung cấp riêng.

## Cài đặt và chạy

Dùng Python 3.11 trở lên. Mở terminal tại thư mục `06. SVM/` và cài thư viện.

```powershell
python -m pip install -r requirements.txt
```

Trong **VS Code**, mở `06. SVM/` làm thư mục làm việc. Đặt `jupyter.notebookFileRoot` thành `${workspaceFolder}` trong Workspace Settings. Mở từng notebook, chọn kernel Python vừa cài thư viện rồi bấm **Run All**.

Trong **Jupyter Notebook**, khởi động bằng `python -m notebook` và mở các notebook trong `code/`. Nếu kernel đang làm việc trong `code/`, chạy `%cd ..` trong một cell tạm trước khi chạy các cell của bài. Mã mẫu dùng đường dẫn tương đối `data/...`, nên thư mục làm việc cần là `06. SVM/`.

Hai notebook đã lưu sẵn kết quả. Bài 6 đo thời gian `.fit()` trên máy chạy, nên số giây và tỉ lệ có thể thay đổi khi chạy lại.

## Kết quả 5 bước thực hành

| Bước | Kết quả chính |
|---|---|
| 1. Lề rộng nhất | Lề `2.2126`, có 3 vectơ hỗ trợ. |
| 2. Tham số C và chuẩn hoá | Với `C` từ `0.01` đến `100`, số vectơ hỗ trợ giảm từ 74 xuống 27. Với ba đặc trưng sinh viên, chuẩn hoá giúp accuracy kiểm tra tăng từ `0.6000` lên `0.9000`. |
| 3. Kernel | Thêm đặc trưng `x²` giúp phân đúng 14/14 điểm mẫu. Trên hai vầng trăng, SVM tuyến tính đạt `0.8667`, RBF và KNN cùng đạt `0.9200`. |
| 4. Dò lưới | Chọn `C=10, gamma=1`, accuracy kiểm định chéo `0.8711`, accuracy kiểm tra `0.9200`. |
| 5. Chữ số viết tay | SVM RBF đạt `0.9911`, sai 4 trong 450 ảnh kiểm tra. |

## Kết quả 6 bài tập

| Bài | Kết quả chính |
|---|---|
| 1. Khoảng cách đến ranh giới | Từ hệ số đã in, hai điểm mới cách ranh giới `1.3966` và `1.0319`. Ba vectơ hỗ trợ cách khoảng `1.1063`, xấp xỉ nửa lề. |
| 2. Thêm một điểm | Điểm `(-1, -1)` ở ngoài lề nên ranh giới giữ nguyên. Điểm `(4.5, 4)` thành vectơ hỗ trợ mới và lề thu từ `2.2126` xuống `0.7339`. |
| 3. Kernel đa thức | Bậc 3 tốt nhất trong ba bậc thử, với `C=1`, accuracy kiểm định chéo `0.8178` và accuracy kiểm tra `0.8267`. RBF ở Bước 4 đạt `0.9200` trên tập kiểm tra. |
| 4. Dò lưới mịn | Chọn `C=30, gamma=1`. Accuracy kiểm định chéo tăng lên `0.8756`, accuracy kiểm tra vẫn `0.9200`. |
| 5. Ma trận nhầm lẫn | Bốn cặp thật → đoán là `9 → 3`, `8 → 1`, `4 → 8`, `7 → 9`. Ảnh từng lỗi nằm trong `figures/`. |
| 6. Đo tốc độ huấn luyện | Với hai lần tăng gấp đôi số mẫu (5.000 → 10.000 và 10.000 → 20.000), thời gian của SVC tăng 18.64 và 2.56 lần, còn LinearSVC tăng 1.97 và 2.38 lần. Số đo là trung vị của ba lượt fit ở mỗi cỡ. |
