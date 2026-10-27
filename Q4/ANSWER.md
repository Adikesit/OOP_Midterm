# Q4 — Your answer

## 1. Predicted output

### Java (`Dispatch.java`)

```text
machine 30 min / a machine
washer 50 min / a machine
dryer 50 min / a machine
a dryer / a machine / dryer
dryer 40 min
Exception in thread "main" java.lang.ClassCastException: class Washer cannot be cast to class Dryer ...
```

- Baris 1–3: loop `room`, setiap `describe()` memanggil `name()` dan `minutes(5)`
  yang didispatch pada tipe runtime (Machine=30, Washer=40+5·2=50, Dryer=60−2·5=50),
  sedangkan `kind(m)` selalu "a machine" karena argumennya bertipe `Machine`.
- Baris 4: `kind(d)` dipilih versi `kind(Dryer)` (tipe compile-time `d` adalah
  `Dryer`) → "a dryer"; `kind(m)` versi `kind(Machine)` → "a machine";
  `m.name()` tetap dispatch dinamis → "dryer".
- Baris 5: setelah `((Dryer) m).setHeat(4)`, `minutes(5)` = 60−4·5 = 40.
- Baris terakhir: `w` menunjuk objek `Washer` (dibuat via `new Washer()`), jadi
  `(Dryer) w` lolos kompilasi (downcast) tetapi gagal saat runtime →
  `ClassCastException`, program langsung berhenti.

### Python (`dispatch.py`)

```text
machine 30 min / a machine
washer 50 min / a machine
dryer 50 min / a dryer
a dryer / a dryer / dryer
dryer 40 min
AttributeError: 'Washer' object has no attribute 'set_heat'
```

- Baris 1–2 sama seperti Java (Machine/Washer bukan Dryer, jadi `isinstance`
  gagal → "a machine"), tetapi baris ke-3 berbeda: `kind()` di Python hanya satu
  fungsi yang memeriksa `isinstance` pada tipe *runtime* objek, sehingga objek
  `Dryer` di loop pun menghasilkan "a dryer" (di Java versi overload
  `kind(Machine)` yang terpilih karena tipe compile-time).
- Baris terakhir: tidak ada compiler yang melarang; `w` adalah objek `Washer`
  yang tidak punya atribut/metode `set_heat`, sehingga error baru muncul saat
  dipanggil (runtime).

## 2. Static overloading vs dynamic dispatch

`kind(Machine)` dan `kind(Dryer)` adalah **overloading**: kedua versi ada di
compile-time dan Java memilih berdasarkan **tipe referensi (compile-time)**.
Karena `m` dideklarasikan `Machine`, `kind(m)` selalu memanggil
`kind(Machine)` → "a machine", meskipun objek aslinya `Dryer`.

Sebaliknya, `m.name()` / `m.minutes()` adalah **overriding**: hanya satu definisi
per kelas, dan JVM memilih versi berdasarkan **tipe objek aslinya (runtime)**.
`m` menunjuk objek `Dryer`, jadi `m.name()` menjalankan `Dryer.name()`.
Perbedaan inilah inti dynamic dispatch (polymorphism), sedangkan overloading
murni diputuskan statis oleh compiler.

(Di Python keduanya otomatis dinamis: tidak ada overloading berdasarkan tipe
parameter, dan `kind()` sendiri harus melihat `isinstance` — tipe runtime.)

## 3. The bad cast

`Machine w = room[1];` menyimpan objek `Washer`. Pernyataan
`Dryer wrong = (Dryer) w;` diizinkan compiler karena setiap `Machine` *bisa jadi*
sebuah `Dryer` (downcast), tetapi saat runtime JVM memeriksa tipe objek sebenarnya,
menemukan `Washer` yang bukan subclass `Dryer`, lalu melempar
`ClassCastException` — dan program berhenti.

Padanan Python tidak punya cast maupun pemeriksaan compile-time; `w.set_heat(4)`
barulah gagal di runtime dengan `AttributeError: 'Washer' object has no attribute
'set_heat'`. Perbedaannya: Java mendeteksi ketidakcocokan tipe saat operasi cast
itself (sementara Python hanya gagal ketika atribut benar-benar dipakai), dan
errornya berbeda (`ClassCastException` vs `AttributeError`).

