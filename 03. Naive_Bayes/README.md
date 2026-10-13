# Lab 03: Naive Bayes
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)


* **Họ và tên:** Huỳnh Hữu Phúc
* **MSSV:** 2474802010314
* **Môn:** Học Máy Và Ứng Dụng
* **LHP:** 261_71ITAI41203_0101
* **GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))

---

## Nội dung

Bài làm gồm hai notebook trong `code/`:

1. **`Lab03_̀5buoc_HuynhHuuPhuc_2474802010314.ipynb`:** năm bước thực hành: định lý Bayes, túi từ, lọc tin rác, làm trơn Laplace và GaussianNB. Các cell mã dùng năm đoạn mẫu trong tài liệu `Lab03_Naive_Bayes.pdf` được cung cấp cho bài học; chỉ sửa ký tự bị lỗi khi trích PDF để mã Python chạy được. PDF gốc không nằm trong thư mục dự án này.
2. **`Lab03_BaiTap.ipynb`:** lời giải sáu bài tập ở mục 7 của tài liệu, kèm kết quả và nhận xét.

## Cấu trúc thư mục

```text
03. Naive_Bayes/
├── README.md
├── requirements.txt
├── code/
│   ├── Lab03_̀5buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab03_BaiTap.ipynb
├── data/
│   ├── tin_nhan.csv      # 300 tin nhắn: 180 thường, 120 rác
│   └── sinh_vien.csv     # 120 sinh viên: 49 rớt, 71 qua
├── figures/              # Hiện trống; script tạo khi chạy, Git không lưu thư mục trống
├── outputs/
│   ├── Lab03_̀5buoc_HuynhHuuPhuc_2474802010314.txt
│   └── Lab03_BaiTap.txt
└── scripts/
    └── run_all.py        # Chạy cả hai notebook
```

Hai file CSV trong `data/` là dữ liệu đầu vào bắt buộc và trùng nội dung với các file CSV ở thư mục Lab 3 bên ngoài. Mã trong notebook dùng đường dẫn tương đối `data/tin_nhan.csv` và `data/sinh_vien.csv`.

## Cài đặt và chạy

Yêu cầu Python 3.10 trở lên. Mở terminal **tại thư mục `03. Naive_Bayes`**, sau đó chạy:

```powershell
python -m pip install -r requirements.txt
python scripts/run_all.py
```

`run_all.py` dùng chính Python đang chạy lệnh để tạo kernel tạm. Script chạy lần lượt hai notebook, lưu kết quả vào các file `.ipynb` trong `code/` và ghi log văn bản vào `outputs/`. Nếu một cell lỗi, script dừng và ghi phần kết quả đã có vào log tương ứng.

Cũng có thể mở từng notebook trong Jupyter hoặc VS Code và chọn **Run All**. Khi chạy cách này, hãy đặt thư mục làm việc là `03. Naive_Bayes` để tìm thấy `data/`. Hai notebook đã có kết quả của các cell: 5 cell mã ở notebook thực hành và 6 cell mã ở notebook bài tập, không có cell báo lỗi.

## Kết quả chính

| Phần | Kết quả |
|---|---|
| Ví dụ Bayes xét nghiệm | `P(bệnh | dương tính) = 0.5000` |
| Túi từ | Ma trận `300 × 40` |
| Bộ lọc tin rác | Train 225, test 75; TN=45, FP=0, FN=4, TP=26; accuracy `0.9467`, precision `1.0000`, recall `0.8667` |
| GaussianNB so với hồi quy logistic | Cả hai đạt accuracy `0.9000` trên dữ liệu sinh viên |

**Lưu ý về mã gốc:** ở bước lọc tin rác, đoạn mẫu trong PDF tạo từ điển bằng toàn bộ 300 tin trước khi chia train/test. Notebook giữ đúng trình tự đó để khớp mã mẫu và kết quả của tài liệu; khi đánh giá mô hình trên dữ liệu mới, nên học từ điển chỉ từ tập train.

### Sáu bài tập

| Bài | Kết quả tóm tắt |
|---|---|
| 1. Bayes với ba nguyên nhân | Hậu nghiệm học đều `0.6376`, học dồn `0.2819`, ít học `0.0805`; tổng bằng `1.0000`. |
| 2. Từ đặc trưng | Rác: mãi, tay, ngay, miễn, trúng. Thường: lớp, em, bài, báo, phòng. |
| 3. Đổi alpha | Với cả năm giá trị từ `0.001` đến `100`, accuracy `0.9467`, precision `1.0000`, recall `0.8667` trên tập kiểm tra này. |
| 4. Bộ lọc tự viết | Accuracy `0.9467`, bằng `MultinomialNB`; cả 75 dự đoán đều trùng nhau. |
| 5. Chọn sai biến thể | MultinomialNB `0.8000`, GaussianNB `0.9000` trên dữ liệu sinh viên. |
| 6. Lớp rác hiếm | Với 180 tin thường và 20 tin rác: accuracy `0.9800`, recall rác `0.8000`; vẫn lọt 1 trong 5 tin rác ở tập kiểm tra. |

Khi dùng bộ dữ liệu mất cân bằng ở bài 6, cần xem recall và số tin rác bị bỏ sót cùng với accuracy. Các con số trên là kết quả của đúng hai file CSV đi kèm và cách chia dữ liệu trong notebook.
