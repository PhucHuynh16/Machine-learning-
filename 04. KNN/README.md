# Lab 04: K láng giềng gần nhất

- **Môn học:** Học máy và ứng dụng
- **Sinh viên:** Huỳnh Hữu Phúc
- **MSSV:** 2474802010314

## Nội dung

Bài làm gồm hai notebook trong `code/`:

1. **`Lab04_5buoc_HuynhHuuPhuc_2474802010314.ipynb`:** năm bước thực hành về khoảng cách Euclid, chuẩn hóa, chọn số láng giềng, so sánh mô hình và KNN hồi quy. Các cell mã giữ nguyên năm đoạn mẫu trong `Lab04_KNN.pdf`; chỉ sửa ký tự bị lỗi khi trích PDF để mã Python chạy được.
2. **`Lab04_BaiTap.ipynb`:** lời giải sáu bài tập ở mục 7 của tài liệu, kèm kết quả và nhận xét.

## Cấu trúc thư mục

```text
04. KNN/
├── README.md
├── requirements.txt
├── code/
│   ├── Lab04_5buoc_HuynhHuuPhuc_2474802010314.ipynb
│   └── Lab04_BaiTap.ipynb
├── data/
│   ├── sinh_vien_mo_rong.csv
│   ├── hai_vang_trang.csv
│   └── gia_nha.csv
├── figures/              # Dành cho hình nếu cần bổ sung
├── outputs/              # Nhật ký kết quả dạng văn bản
└── scripts/
    └── run_all.py        # Chạy cả hai notebook
```

Ba file CSV trong `data/` là dữ liệu đầu vào bắt buộc và trùng nội dung với các file được cung cấp ở thư mục Lab 4 bên ngoài. Mã trong notebook dùng đường dẫn tương đối `data/...`.

## Cài đặt và chạy

Yêu cầu Python 3.10 trở lên. Mở terminal **tại thư mục `04. KNN`**, sau đó chạy:

```powershell
python -m pip install -r requirements.txt
python scripts/run_all.py
```

`run_all.py` dùng chính Python đang chạy lệnh để tạo kernel tạm. Script chạy lần lượt hai notebook, lưu kết quả vào các file `.ipynb` trong `code/` và ghi log văn bản vào `outputs/`. Nếu một cell lỗi, script dừng và ghi phần kết quả đã có vào log tương ứng.

Cũng có thể mở từng notebook trong Jupyter hoặc VS Code và chọn **Run All**. Khi chạy cách này, hãy mở cả thư mục `04. KNN` làm workspace để đường dẫn `data/...` được nhận đúng. Hai notebook bàn giao đã lưu sẵn output và không có cell báo lỗi.

## Kết quả chính của năm bước thực hành

| Phần | Kết quả |
|---|---|
| Khoảng cách trước chuẩn hóa | `d(A,B)=102.2`, `d(A,C)=3000.0` |
| Khoảng cách sau chuẩn hóa | `d(A,B)=3.85`, `d(A,C)=1.79` |
| Ba cột, không chuẩn hóa | Accuracy `0.5333` |
| Ba cột, có chuẩn hóa | Accuracy `0.8667` |
| Bỏ cột chi tiêu, có chuẩn hóa | Accuracy `0.9000` |
| Chọn k bằng kiểm định chéo | `k=13`, test accuracy `0.9200` |
| So sánh trên hai vầng trăng | Logistic `0.8533`, Naive Bayes `0.8533`, KNN `0.9200` |
| Hồi quy giá nhà | KNN MAE `0.4030`, đường thẳng MAE `0.2578` |

## Sáu bài tập

| Bài | Kết quả tóm tắt |
|---|---|
| 1. Tự viết KNN | Accuracy `0.9200`; toàn bộ dự đoán trùng `KNeighborsClassifier`. |
| 2. Khoảng cách Manhattan | Manhattan chọn `k=27`, test accuracy `0.9067`; Euclid chọn `k=13`, đạt `0.9200`. |
| 3. Đổi đơn vị đo | Không chuẩn hóa tăng từ `0.5333` lên `0.8667`; có chuẩn hóa thì đổi đơn vị không làm đổi accuracy. |
| 4. Láng giềng có trọng số | Với `k=101`, accuracy tăng từ `0.8533` lên `0.9067`. |
| 5. Chọn k cho hồi quy | Chọn `k=2`; test MAE `0.4867`, vẫn kém đường thẳng `0.2578`. |
| 6. Đo thời gian | Lấy trung vị 5 lần đo; `.fit` rất nhanh và mốc 100.000 mẫu có `.predict` lâu hơn rõ rệt, thể hiện tính học lười của KNN. |

Thời gian ở bài 6 phụ thuộc máy, phiên bản thư viện và tải hệ thống. Cần so xu hướng tương đối giữa ba cỡ dữ liệu, không so con số tuyệt đối với máy khác.

## Lưu ý phương pháp

- KNN dựa trực tiếp vào khoảng cách nên phải xem xét thang đo và mức liên quan của từng đặc trưng.
- Chuẩn hóa được đặt trong `make_pipeline` để chỉ học trung bình và độ lệch chuẩn từ tập huấn luyện, tránh rò rỉ dữ liệu.
- Số láng giềng được chọn bằng kiểm định chéo trên tập huấn luyện. Tập kiểm tra chỉ được dùng sau khi đã chọn mô hình.
- Bài đo thời gian dùng `algorithm="brute"` để minh họa trực tiếp chi phí so mẫu mới với dữ liệu đã lưu.
