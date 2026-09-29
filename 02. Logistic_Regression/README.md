# Bài 02: Hồi Quy Logistic (Logistic Regression) 📈
> **Môn học:** Học máy và ứng dụng (Machine Learning & Applications)  
> **Tác giả:** Huỳnh Hữu Phúc — **MSSV:** 2474802010314

---

## 📌 Giới thiệu dự án

Dự án này bao gồm toàn bộ nội dung thực hành và bài tập về **Hồi quy logistic (Logistic Regression)** trong bài học 02. Nội dung giúp nắm vững kiến thức cơ bản để xây dựng mô hình phân loại (classification), cụ thể là dự đoán sinh viên qua môn hay rớt môn dựa trên số giờ ôn tập và điểm kiểm tra giữa kỳ.

---

## 📂 Cấu trúc thư mục

```text
Lab02_Hoi_quy_logistic/
├── code/
│   ├── Lab02_1_HuynhHuuPhuc_2474802010314.ipynb  # 6 bước cơ bản Hồi quy logistic
│   └── Lab02_2_BaiTap.ipynb                      # 6 bài tập thực hành mở rộng
├── data/
│   └── sinh_vien.csv                             # Dữ liệu mẫu (gio_on, diem_giua_ky, qua_mon)
├── figures/                                      # Thư mục lưu biểu đồ xuất ra từ notebook
├── outputs/                                      # Thư mục lưu nhật ký chạy kết quả (.txt)
├── scripts/
│   └── run_all.py                                # Script tự động hóa chạy toàn bộ notebook
└── requirements.txt                              # Danh sách các thư viện Python cần thiết
```

---

## 📑 Nội dung chi tiết

### 1. Notebook 1: `Lab02_1_HuynhHuuPhuc_2474802010314.ipynb` (6 bước cơ bản)
Nội dung từng bước xây dựng mô hình Hồi quy logistic:
- **Bước 1:** Đọc dữ liệu và xem qua một lượt (`data/sinh_vien.csv`).
- **Bước 2:** Tự cài đặt hàm sigmoid.
- **Bước 3:** Khớp mô hình bằng thư viện `scikit-learn` (`LogisticRegression`).
- **Bước 4:** Đánh giá mô hình (Ma trận nhầm lẫn, Accuracy, Precision, Recall, F1).
- **Bước 5:** Đổi ngưỡng quyết định.
- **Bước 6:** Thêm biến đầu vào thứ hai (Mô hình hai biến).

---

### 2. Notebook 2: `Lab02_2_BaiTap.ipynb` (6 bài tập thực hành)
Nội dung các bài tập củng cố & nâng cao:
- **Bài tập 1:** Thống kê tỷ lệ qua môn theo nhóm điểm giữa kỳ từ 7 trở lên.
- **Bài tập 2:** Vẽ hàm sigmoid, lưu thành `sigmoid.png`.
- **Bài tập 3:** Viết hàm `du_doan(gio)` in ra z, xác suất và nhãn theo ngưỡng 0.5.
- **Bài tập 4:** Tự tính accuracy, precision, recall, F1 từ TP, TN, FP, FN.
- **Bài tập 5:** Dò ngưỡng từ 0.05 tới 0.95, tìm ngưỡng cho F1 cao nhất.
- **Bài tập 6:** Đổi lớp dương sang lớp rớt môn (`pos_label=0`) rồi đánh giá lại.

---

## 🚀 Hướng dẫn cài đặt & Chạy dự án

### 1. Yêu cầu hệ thống
- **Python 3.9+** (Khuyên dùng Python 3.10 hoặc 3.11)
- Git & Jupyter Notebook / JupyterLab / VS Code Notebook Interface.

### 2. Cài đặt môi trường

1. **Clone repository:** (nếu chưa có)
   ```bash
   git clone <link-repo>
   cd Lab02_Hoi_quy_logistic
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
Bạn có thể mở giao diện Jupyter Notebook để thực hiện từng cell. **Lưu ý: Mở Jupyter từ thư mục gốc của bài (thư mục chứa `data/`) để đường dẫn đọc file được chính xác.**
```bash
jupyter notebook
```
Sau đó truy cập thư mục `code/` và chọn notebook cần chạy:
- `code/Lab02_1_HuynhHuuPhuc_2474802010314.ipynb`
- `code/Lab02_2_BaiTap.ipynb`

#### Cách 2: Chạy tự động hóa toàn bộ bằng Script (`run_all.py`)
Dự án có sẵn script tự động kiểm tra môi trường, thực thi toàn bộ notebook và ghi nhật ký kết quả:
```bash
python scripts/run_all.py
```
*Kết quả đầu ra dạng nhật ký văn bản sẽ được lưu tự động tại thư mục `outputs/` và biểu đồ tại `figures/`.*

---

## 📊 Kết quả & Đánh giá mô hình

- **Bộ dữ liệu:** Bao gồm 120 dòng với các đặc trưng `gio_on`, `diem_giua_ky` và biến mục tiêu `qua_mon` (1 là qua, 0 là rớt).
- **Kết quả chính:**
  - Tỷ lệ qua môn: 0.5917 (71 qua, 49 rớt).
  - Trọng số mô hình một biến: `w = 0.392819`, `b = -5.064890`, mốc 50/50 tại 12.89 giờ.
  - Ma trận nhầm lẫn: TP = 17, TN = 9, FP = 3, FN = 1.
  - Đánh giá: Accuracy 0.8667, Precision 0.8500, Recall 0.9444, F1 0.8947.
  - Accuracy mô hình hai biến: 0.9000.

---

## ⚠️ Lưu ý khi làm bài & Lỗi thường gặp

- Giữ nguyên `random_state=17` và `stratify=y` trong `train_test_split`.
- `X` viết `df[["gio_on"]]` (hai cặp ngoặc vuông), `y` viết `df["qua_mon"]` (một cặp).
- Trong hàm sigmoid phải viết `np.exp(-z)`.
- **Lỗi `FileNotFoundError`:** Đảm bảo chạy code từ thư mục gốc của bài (nơi chứa thư mục `data`).
- **Lỗi `ConvergenceWarning: lbfgs failed to converge`:** Chuẩn hóa bằng `StandardScaler` hoặc tăng `max_iter`.

---

## 🛠️ Thư viện sử dụng

- **[NumPy](https://numpy.org/):** Tính toán đại số tuyến tính & xử lý mảng dữ liệu.
- **[Pandas](https://pandas.pydata.org/):** Đọc, xử lý và phân tích bảng dữ liệu CSV.
- **[Matplotlib](https://matplotlib.org/):** Trực quan hóa biểu đồ và đồ thị.
- **[Scikit-learn](https://scikit-learn.org/):** Huấn luyện mô hình Logistic Regression & đánh giá.
- **[Jupyter Client & NBClient](https://jupyter.org/):** Hỗ trợ tự động hóa thực thi notebook qua script.

---

## 📝 Giấy phép (License)
Dự án được phục vụ cho mục đích học tập và nghiên cứu trong môn học **Học máy và ứng dụng**.
