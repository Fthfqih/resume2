# Seri Studi Kasus 2: Bridging Global Infrastructure to Address Local Challenges with HPC

Repositori ini berisi ringkasan materi, studi kasus, serta implementasi coding untuk **Materi 2** pada kegiatan *Informatics Practitioner Lecture Series* Universitas Bengkulu.

- **Pembicara**: Asst. Prof. Dr. Worawan Diaz Carballo (Thammasat University, Thailand)
- **Topik**: *Bridging Global Infrastructure to Address Local Challenges with HPC*

---

## 📌 Ringkasan Materi

### 1. Apa itu High-Performance Computing (HPC)?
HPC adalah infrastruktur komputasi berskala sangat besar yang mampu melakukan perhitungan matematis berkecepatan tinggi, diukur dalam **FLOPS** (*Floating Point Operations Per Second*).
- **Perkembangan Komputasi**: Dari *Teraflops* hingga *Exaflops* ($10^{18}$ FLOPS).
- **Penggunaan Utama**: Simulasi fisika/molekuler, iklim, model bahasa besar (LLM/AI), dan pemrosesan citra medis.

### 2. Konsep 'The Integrator'
Asst. Prof. Dr. Worawan menekankan pentingnya peran mahasiswa Informatika sebagai **Integrator**:
- Menghubungkan tantangan lokal (*Local Challenges*) dengan teknologi infrastruktur global (*HPC & AI*).
- Menghubungkan para pakar domain (*domain experts* seperti biologi, pertanian, kesehatan) dengan skrip komputasi dan infrastruktur cloud/superkomputer.

### 3. Contoh Studi Kasus Riil
1. **Prakiraan Bencana & Cuaca**: Simulasi dinamika fluida untuk banjir di Bangladesh dan prediksi kualitas udara PM2.5 di Thailand.
2. **Pertanian & Pangan (*DigiFarm*)**: Analisis citra satelit dan drone menggunakan model AI untuk pemetaan penggunaan lahan dan estimasi hasil panen.
3. **Kesehatan & Farmasi**: *Molecular docking* pada tanaman herbal lokal untuk menemukan senyawa aktif obat *asthma spray*.
4. **Bahasa Daerah/Minoritas**: Model *Speech-to-Text* dan *Translation* untuk bahasa suku Hmong.

---

## 🛠️ Studi Kasus Implementation: Simulasi Beban Kerja Paralel (HPC Workload)

Dalam materi ini, diimplementasikan studi kasus **Simulasi Pemrosesan Data Sensor Lingkungan Paralel (Multiprocessing & Parallel Computing)**. Program ini mensimulasikan bagaimana HPC memproses ribuan/jutaan baris data sensor cuaca secara mendatar (*data parallelism*) untuk mendeteksi potensi anomali suhu dan PM2.5.

---

## 🚀 Cara Menjalankan Program

1. **Clone repositori ini atau ekstrak file ZIP.**
2. Pastikan Python 3.8+ sudah terinstal.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan script simulasi pemrosesan paralel:
   ```bash
   python hpc_simulation.py
   ```

---

## 📂 Struktur File

- `README.md`: Dokumen penjelasan materi dan panduan.
- `hpc_simulation.py`: Program Python pemrosesan data paralel menggunakan `multiprocessing`.
- `requirements.txt`: Library pendukung.
