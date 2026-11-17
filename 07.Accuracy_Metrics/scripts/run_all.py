"""Chạy hai notebook Lab 8 và xuất kết quả dạng văn bản."""

import os
from pathlib import Path
import sys
import traceback


def ghi_nhat_ky(notebook, duong_dan):
    """Ghi đầu ra của các cell mã, theo thứ tự bài trong notebook."""
    cac_doan = []
    so_cell = 0
    for cell in notebook.cells:
        if cell.cell_type != "code" or not cell.outputs:
            continue
        so_cell += 1
        cac_doan.append(f"--- Cell mã {so_cell} ---\n")
        for ket_qua in cell.outputs:
            if ket_qua.output_type == "stream":
                cac_doan.append(ket_qua.text)
            elif ket_qua.output_type == "error":
                cac_doan.append("\n".join(ket_qua.traceback) + "\n")
            else:
                noi_dung = ket_qua.get("data", {})
                if "image/png" in noi_dung:
                    cac_doan.append("[Hình hiển thị trong notebook]\n")
                elif "text/plain" in noi_dung:
                    cac_doan.append(noi_dung["text/plain"] + "\n")
        cac_doan.append("\n")
    duong_dan.write_text("".join(cac_doan), encoding="utf-8")


def chay_notebook(notebook, shell, capture_output, tao_ket_qua):
    """Chạy từng cell trong IPython và trả lỗi đầu tiên nếu có."""
    shell.reset(new_session=True)
    cac_cell = [cell for cell in notebook.cells if cell.cell_type == "code"]
    for cell in cac_cell:
        cell.outputs = []
        cell.execution_count = None

    for so_cell, cell in enumerate(cac_cell, start=1):
        with capture_output() as da_in:
            ket_qua = shell.run_cell(cell.source, store_history=False)
        cell.execution_count = so_cell
        loi = ket_qua.error_before_exec or ket_qua.error_in_exec
        if loi is not None:
            cell.outputs.append(tao_ket_qua(
                "error", ename=type(loi).__name__, evalue=str(loi),
                traceback=traceback.format_exception(loi),
            ))
            return loi
        for ten, noi_dung in (("stdout", da_in.stdout), ("stderr", da_in.stderr)):
            if noi_dung:
                cell.outputs.append(tao_ket_qua("stream", name=ten, text=noi_dung))
        for hien_thi in da_in.outputs:
            cell.outputs.append(tao_ket_qua(
                "display_data", data=hien_thi.data, metadata=hien_thi.metadata,
            ))
    return None


def main():
    thu_muc_du_an = Path(__file__).resolve().parents[1]
    cac_notebook = sorted(
        (thu_muc_du_an / "code").glob("*.ipynb"),
        key=lambda p: ("5buoc" not in p.name.lower(), p.name.lower()),
    )
    if len(cac_notebook) != 2:
        print("Thư mục code/ phải có đúng hai notebook.", file=sys.stderr)
        return 1

    du_lieu = ("gia_nha.csv", "sinh_vien_bo_hoc.csv")
    thieu = [ten for ten in du_lieu if not (thu_muc_du_an / "data" / ten).is_file()]
    if thieu:
        print(f"Thiếu dữ liệu trong data/: {', '.join(thieu)}", file=sys.stderr)
        return 1

    try:
        import nbformat
        from IPython.terminal.interactiveshell import TerminalInteractiveShell
        from IPython.utils.capture import capture_output
        from traitlets.config import Config
    except ImportError:
        print(f'Cài thư viện bằng "{sys.executable}" -m pip install -r '
              f'"{thu_muc_du_an / "requirements.txt"}"', file=sys.stderr)
        return 1

    os.chdir(thu_muc_du_an)
    thu_muc_ket_qua = thu_muc_du_an / "outputs"
    thu_muc_ket_qua.mkdir(exist_ok=True)
    (thu_muc_du_an / "figures").mkdir(exist_ok=True)

    # Một luồng đủ cho các bộ dữ liệu nhỏ của lab.
    for bien in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "LOKY_MAX_CPU_COUNT"):
        os.environ.setdefault(bien, "1")
    shell = TerminalInteractiveShell.instance(config=Config({"HistoryManager": {"enabled": False}}))
    with capture_output():
        shell.enable_matplotlib("inline")
    shell.display_formatter.active_types = ["text/plain", "image/png"]

    for duong_dan in cac_notebook:
        print(f"Đang chạy {duong_dan.name}", flush=True)
        notebook = nbformat.read(duong_dan, as_version=4)
        nhat_ky = thu_muc_ket_qua / f"{duong_dan.stem}.txt"
        loi = chay_notebook(notebook, shell, capture_output, nbformat.v4.new_output)
        ghi_nhat_ky(notebook, nhat_ky)
        if loi is not None:
            print(f"Lỗi trong {duong_dan.name}: {loi}", file=sys.stderr)
            print(f"Chi tiết trong {nhat_ky}", file=sys.stderr)
            return 1

        nbformat.validate(notebook)
        ban_tam = duong_dan.with_suffix(".ipynb.tmp")
        nbformat.write(notebook, ban_tam)
        os.replace(ban_tam, duong_dan)
        print(f"  Đã lưu notebook và outputs/{nhat_ky.name}", flush=True)

    print("Hoàn tất hai notebook.")
    return 0


if __name__ == "__main__":
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8")
    raise SystemExit(main())
