import requests

def track_phone(imei):
    api_token = "pk.93ec4f4ae65a325b7d785c02eec583ff"  # Ganti dengan token API yang Anda dapatkan setelah mendaftar di OpenCelliD
    url = f"https://us1.unwiredlabs.com/v2/process.php?token={api_token}&imei={imei}"
    
    response = requests.get(url)
    data = response.json()
    
    if 'status' in data and data['status'] == 'ok':
        latitude = data['lat']
        longitude = data['lon']
        accuracy = data['accuracy']
        print(f"Latitude: {latitude}, Longitude: {longitude}, Accuracy: {accuracy} meters")
    else:
        print("Gagal melacak telepon")

imei_number = "350388632046913"  # Ganti dengan nomor IMEI perangkat yang ingin Anda lacak
track_phone(imei_number)
