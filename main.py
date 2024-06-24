import requests

base_url = "https://api.gios.gov.pl/pjp-api/rest/station"

def get_all_station():
    url = base_url + "/findAll"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"ERROR FETCHING STATIONS: {response.status_code}")

def get_installation_by_station_id(station_id):
    url = base_url + "/sensors/" + station_id
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"ERROR FETCHING INSTALLATIONS FOR STATION {station_id}: {response.status_code}")


def main():
    try:
        stations = get_all_station()

        for station in stations:
            station_id = str(station['id'])
            station_name = station['stationName']

            print("Station #" + station_id + " (" + station_name + "):")

            try:
                installations = get_installation_by_station_id(station_id)
                for installation in installations:
                    installation_id = str(installation['id'])
                    params = installation['param']
                    param_formula = params['paramFormula']

                    print("\tinstallation #" + installation_id + ": ‘" + param_formula + "’")
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()