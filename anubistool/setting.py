v_anubistool = "5.0.0"
v_hamster = "5.0.0"
v_gemz = "5.0.0"
v_dotcoin = "5.0.0"
v_cex = "5.0.0"
v_bunny = "5.0.0"
v_wormfare = "5.0.0"
v_timefarm = "5.0.0"
v_tapswap = "5.0.0"
v_quackquack = "5.0.0"
v_memefi = "5.0.0"
v_yescoin = "5.0.0"

date_dailycombo = "05/07/2024/19/00/00"
morse_hamster = "STAKE"
list_combo = ["ux_ui_team","cx_hub_istanbul"]

def getIP(proxies):
  ip = fakeip = "None"
  url_ip = ["https://api.ipify.org", "https://ipinfo.io/ip", "https://ipv4.icanhazip.com/", "https://api.ipgeolocation.io/getip"]
  error_count = 0
  max_errors = 10
  while (ip == fakeip == "None" or ip == fakeip == " " or fakeip == ip == "") and error_count < max_errors:
    try:
      urlGetIP = random.choice(url_ip)
      ip = requests.get(urlGetIP, timeout=30)
      fakeip = requests.get(urlGetIP, proxies=proxies, timeout=30)
    except Exception as e:
      now_time = datetime.now().strftime("%H:%M:%S")
      print(f"{đỏ}⟨{vàng}{now_time}{đỏ}⟩ Lấy IP thất bại: {e}\n")
      ip = fakeip = "None"
      error_count += 1
      COUNTDOWN(10)
  if error_count >= max_errors:
    print("Quá số lần thử lại. Thoát.")
    return None, None
  try:
    ip = ip.json()["ip"]
    fakeip = fakeip.json()["ip"]
  except:
    ip = ip.text.strip()
    fakeip = fakeip.text.strip()
  return ip, fakeip
