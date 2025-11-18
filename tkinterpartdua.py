import tkinter
import tkinter as padil
import sqlite3


conn = sqlite3.connect("nilai_siswa.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT
)
""")
conn.commit()

root = padil.Tk()
root.title("APLIKASI PREDIKSI PRODI PILIHAN")

var = padil.StringVar()
label = padil.Label(root, textvariable=var, relief=padil.RAISED)
var.set("APLIKASI PREDIKSI PRODI PILIHAN")
label.pack()

frame_input = padil.Frame(root)
frame_input.pack(pady=10)


padil.Label(frame_input, text="Nama Siswa").grid(row=0, column=0, sticky="w", padx=5, pady=3)
entry_nama = padil.Entry(frame_input, width=20)
entry_nama.grid(row=0, column=1, padx=5, pady=3)

padil.Label(frame_input, text="Nilai Biologi").grid(row=1, column=0, sticky="w", padx=5, pady=3)
entry_bio = padil.Entry(frame_input, width=10)
entry_bio.grid(row=1, column=1, padx=5, pady=3)

padil.Label(frame_input, text="Nilai Fisika").grid(row=2, column=0, sticky="w", padx=5, pady=3)
entry_fis = padil.Entry(frame_input, width=10)
entry_fis.grid(row=2, column=1, padx=5, pady=3)

padil.Label(frame_input, text="Nilai Inggris").grid(row=3, column=0, sticky="w", padx=5, pady=3)
entry_ing = padil.Entry(frame_input, width=10)
entry_ing.grid(row=3, column=1, padx=5, pady=3)



def hasil_padil():
    nama = entry_nama.get()
    bio = int(entry_bio.get())
    fis = int(entry_fis.get())
    ing = int(entry_ing.get())

    # LOGIKA PREDIKSI
    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    elif ing > fis and ing > bio:
        prediksi = "Bahasa"
    else:
        prediksi = "tidak ditemukan"

    hasil_label.config(text=f"Hasil Prediksi: {prediksi}")


    cursor.execute("""
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """, (nama, bio, fis, ing, prediksi))

    conn.commit()


tombol = padil.Button(root, text="KIRIM NILAI", command=hasil_padil)
tombol.pack(pady=15)

hasil_label = padil.Label(root, text="", font=("Arial", 12, "bold"))
hasil_label.pack(pady=10)

padil.mainloop()
