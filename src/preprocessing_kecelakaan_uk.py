# Input : dft-road-casualty-statistics-collision-2024.csv
# dft-road-casualty-statistics-road-safety-open-dataset-data-guide-2024.xlsx
# Output: kecelakaan_kepler.csv, top_wilayah.csv

import pandas as pd

# 1. LOAD RAW DATASET
print("Loading dataset...")
df = pd.read_csv('dft-road-casualty-statistics-collision-2024.csv', low_memory=False)
print("Dataset oke.")

# 2. CEK KOORDINAT
print("\nSample koordinat:")
print(df[['longitude', 'latitude']].head(5))


# 3. FEATURE CREATION - Severity Label
# Mapping collision_severity (integer) -> label teks. 1 = Fatal, 2 = Serious, 3 = Slight
print("\nFeature Creation: severity_label...")
severity_map = {1: 'Fatal', 2: 'Serious', 3: 'Slight'}
df['severity_label'] = df['collision_severity'].map(severity_map)

print("Distribusi severity:")
print(df['severity_label'].value_counts())

# 4. EXPORT CSV cuma kolom longitude, latitude, severity_label

print("\nExport CSV untuk Kepler.gl...")
df[['longitude', 'latitude', 'severity_label']].to_csv('kecelakaan_kepler.csv', index=False)
print("File 'kecelakaan_kepler.csv' berhasil disimpan.")

##############################################
#untuk analisis wilayah pake lookup wilayah dari file guide
# 5. load file guide / lookup wilayah
print("\nLoad file data guide...")
df_guide = pd.read_excel(
'dft-road-casualty-statistics-road-safety-open-dataset-data-guide-2024.xlsx',
sheet_name='2024_code_list'
)

# 6. buat lookup table kodde jadi nama wilayah
print("Membuat lookup table wilayah...")
lookup = df_guide[df_guide['field name'] == 'local_authority_ons_district'][['code/format', 'label']]
lookup.columns = ['local_authority_ons_district', 'district_name']
print(f"Total wilayah ditemukan: {len(lookup)}")


# 7. merge nama wilayah ke dataset
print("\nMerge nama wilayah ke dataset...")
df_merged = df.merge(lookup, on='local_authority_ons_district', how='left')


# 8. ambil top 10 wilayah kecelakaan terbanyak
print("\nTop 10 wilayah kecelakaan terbanyak:")
top10 = df_merged['district_name'].value_counts().head(10)
print(top10)

# Export top wilayah ke CSV
top10.reset_index().rename(columns={'index': 'district_name', 'district_name': 'jumlah'}).to_csv(
'top_wilayah.csv', index=False
)
print("\nFile 'top_wilayah.csv' berhasil disimpan.")

# 9. total kecelakaan london dari semua borough
#Kode E09 = London boroughs
print("\nHitung total kecelakaan London (semua borough)...")
london = df_merged[df_merged['local_authority_ons_district'].str.startswith('E09')]
print(f"Total kecelakaan London: {len(london)}")
print("\nTop 10 borough London:")
print(london['district_name'].value_counts().head(10))


# hasil akhir
print("\n=== Preprocessing selesai ===")
print("Output files:")
print("  - kecelakaan_kepler.csv  -> untuk Kepler.gl (peta sebaran)")
print("  - top_wilayah.csv-> untuk analisis wilayah")
