"""Chạy các notebook trong code/, lưu kết quả và nhật ký bằng một lệnh."""

import json
import os
from pathlib import Path
import sys
import tempfile


def ghi_nhat_ky(notebook, duong_dan):
    """Lưu phần kết quả dạng chữ; hình vẫn nằm trong notebook và figures/."""
    cac_doan = []
    for so_cell, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type != "code":
            continue
        cac_doan.append(f"--- Cell {so_cell} ---\n")
        for ket_qua in cell.get("outputs", []):
            if ket_qua.output_type == "stream":
                cac_doan.append(ket_qua.text)
            elif ket_qua.output_type in ("execute_result", "display_data"):
                noi_dung = ket_qua.get("data", {})
                if "image/png" in noi_dung:
                    cac_doan.append("[Biểu đồ hiển thị trong notebook]\n")
                elif "text/plain" in noi_dung:
                    cac_doan.append(noi_dung["text/plain"] + "\n")
            elif ket_qua.output_type == "error":
                cac_doan.append(f"{ket_qua.ename}: {ket_qua.evalue}\n")
        cac_doan.append("\n")
    duong_dan.write_text("".join(cac_doan), encoding="utf-8")


def main():
    # Dựa vào vị trí script, không phụ thuộc nơi người dùng mở terminal.
    thu_muc_du_an = Path(__file__).resolve().parents[1]
    thu_muc_ket_qua = thu_muc_du_an / "outputs"
    cac_notebook = sorted(
        (thu_muc_du_an / "code").glob("*.ipynb"),
        key=lambda p: (not p.name.lower().startswith("lab"), p.name.lower()),
    )
    if not cac_notebook:
        print("Không tìm thấy notebook trong thư mục code/.", file=sys.stderr)
        return 1
    if not (thu_muc_du_an / "data" / "gia_nha.csv").is_file():
        print("Thiếu data/gia_nha.csv. Hãy tải đầy đủ thư mục dự án.", file=sys.stderr)
        return 1

    try:
        import nbformat
        from nbclient import NotebookClient
        from jupyter_client import KernelManager
        from jupyter_client.kernelspec import KernelSpecManager
    except ImportError:
        print("Chưa đủ thư viện. Cài bằng lệnh sau rồi chạy lại:", file=sys.stderr)
        print(f'"{sys.executable}" -m pip install -r "{thu_muc_du_an / "requirements.txt"}"', file=sys.stderr)
        return 1

    thu_muc_ket_qua.mkdir(exist_ok=True)
    (thu_muc_du_an / "figures").mkdir(exist_ok=True)

    # Kernel tạm dùng đúng Python đang chạy script, không đổi cấu hình Jupyter.
    with tempfile.TemporaryDirectory(prefix="hoi_quy_kernel_") as tam:
        thu_muc_kernel = Path(tam) / "python3"
        thu_muc_kernel.mkdir()
        cau_hinh = {
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Python 3",
            "language": "python",
            "env": {"MPLBACKEND": "module://matplotlib_inline.backend_inline"},
        }
        (thu_muc_kernel / "kernel.json").write_text(json.dumps(cau_hinh), encoding="utf-8")

        for duong_dan in cac_notebook:
            print(f"Đang chạy: {duong_dan.name}", flush=True)
            notebook = nbformat.read(duong_dan, as_version=4)
            nhat_ky = thu_muc_ket_qua / f"{duong_dan.stem}.txt"
            quan_ly_kernel = KernelManager(
                kernel_name="python3",
                kernel_spec_manager=KernelSpecManager(kernel_dirs=[tam]),
            )
            try:
                # Mỗi notebook có kernel riêng; dừng nếu một cell báo lỗi.
                NotebookClient(
                    notebook,
                    km=quan_ly_kernel,
                    timeout=300,
                    resources={"metadata": {"path": str(thu_muc_du_an)}},
                ).execute(cleanup_kc=True)
            except Exception as loi:
                ghi_nhat_ky(notebook, nhat_ky)
                print(f"Lỗi khi chạy {duong_dan.name}: {loi}", file=sys.stderr)
                print(f"Xem nhật ký: {nhat_ky}", file=sys.stderr)
                return 1

            # Chỉ cập nhật notebook gốc khi toàn bộ cell đã chạy thành công.
            ban_tam = duong_dan.with_suffix(".ipynb.tmp")
            nbformat.write(notebook, ban_tam)
            os.replace(ban_tam, duong_dan)
            ghi_nhat_ky(notebook, nhat_ky)
            print(f"  Đã lưu notebook và outputs/{nhat_ky.name}", flush=True)

    print(f"Hoàn tất {len(cac_notebook)} notebook. Biểu đồ nằm trong: {thu_muc_du_an / 'figures'}")
    return 0


if __name__ == "__main__":
    # Hiển thị tiếng Việt trên terminal Windows, kể cả khi chuyển hướng stdout.
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8")
    raise SystemExit(main())
