import requests

def track_phone(imei):
    url = f"https://us1.unwiredlabs.com/v2/process.php?token=pk.93ec4f4ae65a325b7d785c02eec583ff&imei={imei}"
    response = requests.get(url)
    data = response.json()
    
    if 'status' in data and data['status'] == 'ok':
        latitude = data['lat']
        longitude = data['lon']
        accuracy = data['accuracy']
        print(f"Latitude: {latitude}, Longitude: {longitude}, Accuracy: {accuracy} meters")
    else:
        print("Gagal melacak telepon")

# Ganti 'YOUR_API_TOKEN' dengan token API yang Anda dapatkan setelah mendaftar di OpenCelliD

imei_number = "86913003490637"  # Ganti dengan nomor IMEI perangkat yang ingin Anda lacak
track_phone(imei_number)
