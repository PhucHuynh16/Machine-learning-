# Lab 07 - Đánh giá mô hình

- **Môn học** Học máy ứng dụng
- **Giảng viên biên soạn** ThS. Nguyễn Thái Anh
- **Sinh viên** Huỳnh Hữu Phúc
- **MSSV** 2474802010314

## Nội dung và cấu trúc

Notebook thực hành giữ sáu đoạn mã mẫu ở các mục 2–7 của tài liệu `Lab07_DanhGiaMoHinh.pdf` được cung cấp riêng. Dấu gạch nối trong mã được phục hồi khi trích PDF. Sau mỗi đoạn có kết quả đã chạy và nhận xét. Notebook bài tập giải sáu câu ở mục 8, theo thứ tự đề bài, mã, kết quả và giải thích.

```text
07.Accuracy_Metrics/
├── README.md
├── requirements.txt
├── code/
│   ├── Lab07_6buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab07_BaiTap.ipynb
├── data/
│   ├── sinh_vien_bo_hoc.csv
│   └── gia_nha.csv
├── figures/
│   └── roc.png
├── outputs/
│   ├── Lab07_6buoc_HuynhHuuPhuc_2474802010314.txt
│   └── Lab07_BaiTap.txt
└── scripts/
    └── run_all.py
```

## Dữ liệu

| Nguồn | Nội dung và cách dùng |
|---|---|
| `data/sinh_vien_bo_hoc.csv` | 1.200 mẫu mô phỏng, gồm 1.081 bạn học tiếp (lớp 0) và 119 bạn bỏ học (lớp 1). Bốn biến đầu vào là `diem_tb`, `so_buoi_vang`, `tin_chi_no`, `gio_lam_them`. Sáu bước và các bài 1, 3, 4, 5 dùng chung cách chia phân tầng 75/25 với `random_state=17`. |
| `data/gia_nha.csv` | 60 căn, giá tính bằng tỷ đồng. Bài 6 giữ mô hình theo `dien_tich` và cách chia 80/20 với `random_state=42` của bước đánh giá ở Lab 1. |
| `load_digits()` | 1.797 ảnh chữ số 8 × 8 có sẵn trong scikit-learn. Bài 2 dùng SVM RBF và cùng cách chia dữ liệu với Lab 6. |

Hai tệp CSV trong `data/` khớp từng byte với dữ liệu trong ZIP của Lab 7.

## Cài đặt và chạy

Yêu cầu Python 3.11 trở lên. Kết quả trong notebook được kiểm tra với Python 3.14.3 và các phiên bản thư viện ghi trong `requirements.txt`.

1. Mở terminal tại thư mục `07.Accuracy_Metrics/` và cài thư viện.

   ```powershell
   python -m pip install -r requirements.txt
   ```


Sau khi cài, chọn một trong hai cách chạy.

- Trong **VS Code**, mở riêng thư mục `07.Accuracy_Metrics/` làm workspace. Đặt `jupyter.notebookFileRoot` thành `${workspaceFolder}` trong Workspace Settings, chọn kernel Python vừa cài rồi bấm **Run All** cho từng notebook.
- Trong **Jupyter Notebook**, chạy `python -m notebook` từ `07.Accuracy_Metrics/` và mở notebook trong `code/`. Nếu `%pwd` cho biết kernel đang ở `07.Accuracy_Metrics/code/`, chạy `%cd ..` trong một cell tạm ở đầu notebook trước khi chạy các cell của bài. Thư mục làm việc cần là `07.Accuracy_Metrics/` để mã gốc đọc được `data/...` và Bài 4 ghi `figures/roc.png` đúng chỗ.

Mỗi notebook chạy độc lập. Khi chạy lại, scikit-learn 1.9.0 có thể in `FutureWarning` cho `SVC(probability=True)` ở Bước 5 và Bài 5. Tham số này được giữ để dùng đúng mô hình mẫu, và các cell vẫn chạy xong.

## Kết quả 6 bước thực hành

| Bước | Kết quả chính |
|---|---|
| 1. Khi accuracy đánh lừa | Mô hình lười đạt `0.9000` nhưng phát hiện 0/30 ca bỏ học. Logistic đạt `0.9467` và phát hiện 17/30 ca. |
| 2. Ma trận nhầm lẫn | Logistic có TN = 267, FP = 3, FN = 13 và TP = 17. Tổng cộng 20 cảnh báo. |
| 3. Precision, recall và F1 | Kết quả tính tay và scikit-learn khớp nhau, lần lượt là `0.8500`, `0.5667` và `0.6800` cho lớp bỏ học. |
| 4. Đổi ngưỡng | Tối ưu F1 trên dự đoán ngoài fold từ tập học chọn ngưỡng `0.25`. F1 kiểm tra `0.7077`, recall kiểm tra `0.7667`. |
| 5. ROC và AUC | Logistic có AUC cao nhất trong sáu mô hình, đạt `0.9449`. Rừng ngẫu nhiên đạt `0.9249`. |
| 6. Kiểm định chéo và cân bằng lớp | Kiểm định chéo 5 phần cho accuracy `0.9289` và recall `0.4810`. Cân bằng lớp ở logistic làm recall kiểm tra tăng từ `0.5667` lên `0.8667`, precision giảm từ `0.8500` xuống `0.4483`. |

## Kết quả 6 bài tập

| Bài | Kết quả chính |
|---|---|
| 1. Hàm đánh giá NumPy | Cả bốn thước đo khớp scikit-learn. Với mô hình lười, `TP + FP = 0` nên precision không xác định và được báo cáo là 0 theo quy ước. Notebook giải thích từng ô TN, FP, FN, TP cho cả hai mô hình. |
| 2. Chữ số viết tay | Số 8 có precision và recall thấp nhất, đều là `0.9767`. Tập kiểm tra có 43–46 ảnh mỗi chữ số nên hai kiểu trung bình cho kết quả gần nhau. |
| 3. Recall ít nhất 80% | Ngưỡng lớn nhất từ xác suất ngoài fold là khoảng `0.1717736449`, đạt recall `72/89 = 0.8090` trên dự đoán ngoài fold. Áp dụng ngưỡng cố định cho tập kiểm tra được recall `24/30 = 0.8000`, precision `24/47 = 0.5106`, 47 cảnh báo. |
| 4. Tự vẽ ROC | Logistic có AUC cao hơn. Hai đường đổi thứ tự theo FPR và có giao nhau. [Mở biểu đồ ROC](figures/roc.png). |
| 5. Cân bằng lớp | Ở ngưỡng xác suất `0.5`, rừng ngẫu nhiên thay đổi nhiều hơn theo tổng độ lệch tuyệt đối của ba chỉ số. Recall của rừng tăng từ `0.5667` lên `0.7000`, còn SVM giảm từ `0.5000` xuống `0.4333`. |
| 6. Một dự đoán giá nhà lệch 5 tỷ | MAE tăng `0.2578 → 0.6745` tỷ, RMSE tăng `0.3730 → 1.5505` tỷ, R² giảm `0.9622 → 0.3475`. RMSE tăng mạnh hơn MAE vì bình phương sai số trước khi lấy trung bình. |

Bước 4 chọn ngưỡng để tối đa F1. Bài 3 chọn ngưỡng theo yêu cầu recall tối thiểu 80%. Cả hai xác định ngưỡng bằng dự đoán ngoài fold trên tập học.
