# Machine Learning — Học Máy Và Ứng Dụng

Repository lưu mã nguồn, dữ liệu và kết quả các bài thực hành môn Học Máy Và Ứng Dụng tại Trường Đại học Văn Lang.

- **Sinh viên:** Huỳnh Hữu Phúc — MSSV 2474802010314
- **Lớp học phần:** 261_71ITAI41203_0101
- **Giảng viên:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))

## Bài thực hành

| Bài | Chủ đề | Thư mục |
| --- | --- | --- |
| 01 | Hồi quy tuyến tính (dữ liệu giá nhà) | [01. Linear_Regression](01.%20Linear_Regression/README.md) |

## Cấu trúc

```text
Machine-Learning/
├── 01. Linear_Regression/
│   ├── code/           # Notebook
│   ├── data/           # gia_nha.csv
│   ├── figures/        # Biểu đồ
│   ├── outputs/        # Nhật ký kết quả
│   ├── scripts/        # run_all.py
│   └── requirements.txt
└── README.md
```

## Cách chạy

```sh
git clone https://github.com/huyryan220806/Machine-Learning.git
cd "Machine-Learning/01. Linear_Regression"
python -m pip install -r requirements.txt
python scripts/run_all.py
```

Muốn chạy từng cell, mở notebook trong `code/` bằng Jupyter hoặc VS Code. Giữ nguyên các thư mục `code/`, `data/`, `scripts/` khi di chuyển bài.
