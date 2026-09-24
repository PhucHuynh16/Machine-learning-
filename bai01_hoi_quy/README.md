# Bài 01: Hồi Quy Tuyến Tính

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)


* **Họ và tên:** Huỳnh Hữu Phúc
* **MSSV:** 2474802010314
* **Môn:** Học Máy Và Ứng Dụng
* **LHP:** 261_71ITAI41203_0101
* **GVHD:** ThS. Nguyễn Thái Anh ([GitHub](https://github.com/AnhNguyenVLU))

## Nội dung bài thực hành

---

## 📌 Giới thiệu dự án

Dự án này bao gồm toàn bộ nội dung thực hành và bài tập về **Hồi quy tuyến tính (Linear Regression)** trong bài học 01. Nội dung giúp nắm vững kiến thức cơ bản từ công thức toán học, tự cài đặt Gradient Descent cho đến việc sử dụng thư viện chuẩn `scikit-learn` để xây dựng, đánh giá và tối ưu mô hình dự đoán giá nhà.

---

## 📂 Cấu trúc thư mục

```text
Bai01_hoi_quy/
├── code/
│   ├── Lab01_1_HuynhHuuPhuc_2474802010314.ipynb  # 7 bước cơ bản Hồi quy tuyến tính
│   └── Lab01_2_BaiTap.ipynb                      # 6 bài tập thực hành mở rộng
├── data/
│   └── gia_nha.csv                               # Dữ liệu mẫu (diện tích, số phòng, tuổi nhà, giá)
├── figures/                                      # Thư mục lưu biểu đồ xuất ra từ notebook
├── outputs/                                      # Thư mục lưu nhật ký chạy kết quả (.txt)
├── scripts/
│   └── run_all.py                                # Script tự động hóa chạy toàn bộ notebook
├── .gitignore                                    # Cấu hình bỏ qua các file tạm/cache của Git
├── README.md                                     # Tài liệu hướng dẫn dự án
└── requirements.txt                              # Danh sách các thư viện Python cần thiết
```

---

## 📑 Nội dung chi tiết

### 1. Notebook 1: `Lab01_1_HuynhHuuPhuc_2474802010314.ipynb` (7 bước cơ bản)
Nội dung từng bước xây dựng mô hình Hồi quy tuyến tính:
- **Bước 1:** Đọc dữ liệu và khảo sát sơ bộ (`data/gia_nha.csv`).
- **Bước 2:** Định nghĩa & đo lường sai số dự đoán (MSE, RMSE).
- **Bước 3:** Tìm tham số tối ưu $w$ và $b$ bằng công thức đóng (Normal Equation).
- **Bước 4:** Xây dựng mô hình với thư viện `scikit-learn` (`LinearRegression`).
- **Bước 5:** Chia tập dữ liệu Train/Test & đánh giá hiệu năng ($R^2$, MAE, MSE, RMSE).
- **Bước 6:** Tự cài đặt thuật toán **Gradient Descent** để tối ưu hóa tham số từng bước.
- **Bước 7:** Mở rộng mô hình Hồi quy đa biến (thêm thuộc tính số phòng, tuổi nhà).

---

### 2. Notebook 2: `Lab01_2_BaiTap.ipynb` (6 bài tập thực hành)
Nội dung các bài tập củng cố & nâng cao:
- **Bài tập 1:** Lọc và phân tích nhóm căn hộ có diện tích/quy mô lớn.
- **Bài tập 2:** Trực quan hóa quan hệ giữa số phòng và giá nhà bằng biểu đồ phân tán (Scatter plot).
- **Bài tập 3:** Đổi biến đầu vào độc lập sang thuộc tính *Tuổi nhà*.
- **Bài tập 4:** Thêm thuộc tính *Số phòng* vào mô hình hồi quy đa biến.
- **Bài tập 5:** Thử nghiệm & so sánh tốc độ hội tụ của Gradient Descent với các **Learning Rate** khác nhau.
- **Bài tập 6:** Xây dựng hàm dự đoán hoàn chỉnh kèm tính năng **cảnh báo ngoại suy** (Extrapolation Warning) khi dữ liệu nằm ngoài khoảng huấn luyện.

---

## 🚀 Hướng dẫn cài đặt & Chạy dự án

### 1. Yêu cầu hệ thống
- **Python 3.9+** (Khuyên dùng Python 3.10 hoặc 3.11)
- Git & Jupyter Notebook / JupyterLab / VS Code Notebook Interface.

### 2. Cài đặt môi trường

1. **Clone repository:**
   ```bash
   git clone https://github.com/username/Bai01_hoi_quy.git
   cd Bai01_hoi_quy
   ```

2. **Tạo môi trường ảo (khuyên dùng):**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

---

### 3. Chạy dự án

#### Cách 1: Mở và chạy trực tiếp trên Jupyter Notebook / VS Code
Bạn có thể mở giao diện Jupyter Notebook để thực hiện từng cell:
```bash
jupyter notebook
```
Sau đó truy cập thư mục `code/` và chọn notebook cần chạy:
- `code/Lab01_1_HuynhHuuPhuc_2474802010314.ipynb`
- `code/Lab01_2_BaiTap.ipynb`

#### Cách 2: Chạy tự động hóa toàn bộ bằng Script (`run_all.py`)
Dự án có sẵn script tự động kiểm tra môi trường, thực thi toàn bộ notebook và ghi nhật ký kết quả:
```bash
python scripts/run_all.py
```
*Kết quả đầu ra dạng nhật ký văn bản sẽ được lưu tự động tại thư mục `outputs/` và biểu đồ tại `figures/`.*

---

## 📊 Kết quả & Đánh giá mô hình

- **Công thức tính toán:**
  $$\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b$$
- **Hàm mất mát (Mean Squared Error - MSE):**
  $$J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)^2$$
- Các chỉ số đánh giá được tính toán chi tiết trong notebook bao gồm **$R^2$ Score**, **MAE**, **MSE**, và **RMSE**.

---

## 🛠️ Thư viện sử dụng

- **[NumPy](https://numpy.org/):** Tính toán đại số tuyến tính & xử lý mảng dữ liệu.
- **[Pandas](https://pandas.pydata.org/):** Đọc, xử lý và phân tích bảng dữ liệu CSV.
- **[Matplotlib](https://matplotlib.org/):** Trực quan hóa biểu đồ và đồ thị.
- **[Scikit-learn](https://scikit-learn.org/):** Huấn luyện mô hình Linear Regression & chia tập dữ liệu.
- **[Jupyter Client & NBClient](https://jupyter.org/):** Hỗ trợ tự động hóa thực thi notebook qua script.

---

## 📝 Giấy phép (License)
Dự án được phục vụ cho mục đích học tập và nghiên cứu trong môn học **Học máy và ứng dụng**.
