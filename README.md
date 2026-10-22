
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
# Machine Learning — Học Máy Và Ứng Dụng

* **Họ và tên:** Huỳnh Hữu Phúc
* **MSSV:** 2474802010314
* **Môn:** Học Máy Và Ứng Dụng
* **LHP:** 261_71ITAI41203_0101
* **GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))


## Bài thực hành

| Bài | Chủ đề | Thư mục |
| --- | --- | --- |
| 01 | Hồi quy tuyến tính (dữ liệu giá nhà) | [01. Linear_Regression](01.%20Linear_Regression/README.md) |
| 02 | Hồi quy logistic | [02. Logistic_Regression](02.%20Logistic_Regression/README.md) |
| 03 | Naive Bayes | [03. Naive_Bayes](03.%20Naive_Bayes/README.md) |
| 04 | K láng giềng gần nhất (KNN) | [04. KNN](04.%20KNN/README.md) |

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
├── 02. Logistic_Regression/
│   └── README.md
├── 03. Naive_Bayes/
│   ├── code/           # 5 bước thực hành và 6 bài tập
│   ├── data/           # tin_nhan.csv, sinh_vien.csv
│   ├── outputs/        # Nhật ký kết quả
│   ├── scripts/        # run_all.py
│   └── requirements.txt
├── 04. KNN/
│   ├── code/           # 5 bước thực hành và 6 bài tập
│   ├── data/           # 3 bộ dữ liệu CSV
│   ├── figures/
│   ├── outputs/        # Nhật ký kết quả
│   ├── scripts/        # run_all.py
│   ├── README.md
│   └── requirements.txt
└── README.md
```

## Cách chạy

```sh
git clone https://github.com/PhucHuynh16/Machine-learning-.git
cd "Machine-learning-/04. KNN"
python -m pip install -r requirements.txt
python scripts/run_all.py
```

Muốn chạy từng cell, mở notebook trong `code/` bằng Jupyter hoặc VS Code. Giữ nguyên các thư mục `code/`, `data/`, `scripts/` khi di chuyển bài.
