"""
Studi Kasus Materi 2: Parallel Data Processing Simulation (HPC Concept)
Pembicara: Asst. Prof. Dr. Worawan Diaz Carballo
Deskripsi: Mensimulasikan data parallelism dalam pengolahan data sensor lingkungan (Suhu & PM2.5)
           menggunakan Multiprocessing untuk mempercepat komputasi.
"""

import time
import random
import multiprocessing as mp
import pandas as pd

def generate_sensor_data(num_records=100000):
    """Generasi dataset simulasi sensor lingkungan."""
    print(f"Menggenerasi {num_records} data sensor...")
    data = {
        'sensor_id': [f"SENS-{i%500:04d}" for i in range(num_records)],
        'temperature': [random.uniform(20.0, 42.0) for _ in range(num_records)],
        'pm25': [random.uniform(5.0, 180.0) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

def process_chunk(chunk):
    """Fungsi pekerja untuk memproses sekumpulan data (Chunk/Core)."""
    # Deteksi anomali: Suhu > 38C dan PM2.5 > 100
    anomalies = chunk[(chunk['temperature'] > 38.0) & (chunk['pm25'] > 100.0)]
    avg_temp = chunk['temperature'].mean()
    avg_pm25 = chunk['pm25'].mean()
    return len(anomalies), avg_temp, avg_pm25

def main():
    print("=== SIMULASI PEMROSESAN PARALEL HPC (DATA PARALLELISM) ===")
    
    num_records = 200000
    df = generate_sensor_data(num_records)
    
    # 1. Pemrosesan Sekuensial (Single Core)
    print("
--- 1. Pemrosesan Sekuensial (Single Core) ---")
    start_seq = time.time()
    seq_anomalies, seq_avg_temp, seq_avg_pm25 = process_chunk(df)
    end_seq = time.time()
    seq_time = end_seq - start_seq
    print(f"Waktu eksekusi sekuensial: {seq_time:.4f} detik")
    print(f"Anomali terdeteksi: {seq_anomalies}")

    # 2. Pemrosesan Paralel (Multi Core / Simu HPC Cluster)
    print("
--- 2. Pemrosesan Paralel (Multi-Core / HPC Simulation) ---")
    num_cores = mp.cpu_count()
    print(f"Menggunakan {num_cores} CPU cores...")
    
    start_par = time.time()
    chunks = [df[i::num_cores] for i in range(num_cores)]
    
    with mp.Pool(processes=num_cores) as pool:
        results = pool.map(process_chunk, chunks)
        
    par_anomalies = sum(r[0] for r in results)
    end_par = time.time()
    par_time = end_par - start_par
    
    print(f"Waktu eksekusi paralel   : {par_time:.4f} detik")
    print(f"Anomali terdeteksi       : {par_anomalies}")
    
    speedup = seq_time / par_time if par_time > 0 else 1
    print(f"
[HASIL] Acceleration / Speedup factor: {speedup:.2f}x lebih cepat!")

if __name__ == "__main__":
    main()
