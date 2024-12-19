# Gunakan base image Python yang ringan
FROM python:3.10-slim

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Upgrade pip untuk menghindari peringatan
RUN pip install --no-cache-dir --upgrade pip

# Install dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh file proyek ke dalam container
COPY . /app

# Expose port Flask (5000)
EXPOSE 5000

# Perintah untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]
