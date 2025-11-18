import tkinter
import tkinter as padil

root = padil.Tk()
root.title("aplikasi")
var = padil.StringVar()
label = padil.Label(root, textvariable=var, relief=padil.RAISED)
var.set("APLIKASI PREDIKSI PRODI PILIHAN")
label.pack()

frame_input = padil.Frame(root)
frame_input.pack(pady=10)

entries = []
for i in range(10):
    padil.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}").grid(row=i, column=0, sticky="w", padx=5, pady=3)
    entry = padil.Entry(frame_input, width=10)
    entry.grid(row=i, column=1, padx=5, pady=3)
    entries.append(entry)

def hasil_padil():
    hasil_padil.config(text="PRODI TEKNOLOGI INFORMASI")

tombol = padil.Button(root, text="HASIL", command=hasil_padil)
tombol.pack(pady=15)

hasil_padil = padil.Label()
hasil_padil.pack(pady=10)

padil.mainloop()