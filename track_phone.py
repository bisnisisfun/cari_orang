import requests

def track_phone(imei):
    api_url = f"https://p3t.pdsi.lapan.go.id/api/v1/location/imei/{imei}"
    headers = {"Authorization": "Bearer pk.93ec4f4ae65a325b7d785c02eec583ff"}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        if 'latitude' in data and 'longitude' in data:
            latitude = data['latitude']
            longitude = data['longitude']
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("Data lokasi tidak ditemukan")
    else:
        print("Gagal melacak perangkat")

imei_number = "369130033490637"  # Ganti dengan nomor IMEI perangkat yang ingin Anda lacak
track_phone(imei_number)
