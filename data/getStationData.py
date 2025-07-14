import wikipediaapi
import re

def get_station_coordinates(station_name, lang='en'):
    wiki_wiki = wikipediaapi.Wikipedia(lang)
    page = wiki_wiki.page(station_name)

    if not page.exists():
        print(f"页面 {station_name} 不存在。")
        return None

    # 提取页面摘要或原文中的经纬度格式，如: 35°41′30″N 139°41′40″E
    coord_pattern = r'(\d+)[°º]\s*(\d+)?[′']?\s*(\d+)?[″"]?\s*([NS])\s*(\d+)[°º]\s*(\d+)?[′']?\s*(\d+)?[″"]?\s*([EW])'
    match = re.search(coord_pattern, page.text)

    if match:
        lat_deg = int(match.group(1))
        lat_min = int(match.group(2) or 0)
        lat_sec = int(match.group(3) or 0)
        lat_dir = match.group(4)

        lon_deg = int(match.group(5))
        lon_min = int(match.group(6) or 0)
        lon_sec = int(match.group(7) or 0)
        lon_dir = match.group(8)

        def dms_to_dd(deg, minutes, seconds, direction):
            dd = deg + minutes / 60 + seconds / 3600
            if direction in ['S', 'W']:
                dd *= -1
            return dd

        latitude = dms_to_dd(lat_deg, lat_min, lat_sec, lat_dir)
        longitude = dms_to_dd(lon_deg, lon_min, lon_sec, lon_dir)

        return latitude, longitude
    else:
        print("未找到经纬度。可能该页面没有包含坐标。")
        return None

# 示例用法
station = "Tokyo Station"
coords = get_station_coordinates(station)
if coords:
    print(f"{station} 的经纬度是: {coords}")
