import requests

base_url = "https://api.gios.gov.pl/pjp-api/rest/station"

def get_all_station():
    url = base_url + "/findAll"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"ERROR FETCHING STATIONS: {e}")

def get_installation_by_station_id(station_id):
    url = base_url + "/sensors/" + station_id
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"ERROR FETCHING INSTALLATIONS FOR STATION {station_id}: {e}")


def main():
    try:
        stations = get_all_station()

        for station in stations:
            station_id = str(station['id'])
            station_name = station['stationName']

            print(f"Station #{station_id} ({station_name}):")

            try:
                installations = get_installation_by_station_id(station_id)

                if not installations:
                    print(f"\tNo installations found for station #{station_id}")
                    continue

                for installation in installations:
                    installation_id = str(installation['id'])
                    param_formula = installation['param']['paramFormula']

                    print(f"\tinstallation #{installation_id}: ‘{param_formula}’")
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
