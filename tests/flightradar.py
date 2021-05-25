import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
urls1 = {
    'Alor Island Airport': 'https://www.flightradar24.com/data/airports/ard/arrivals',
    'Ambon Pattimura Airport': 'https://www.flightradar24.com/data/airports/amq/arrivals',
    'Atambua Haliwen Airport': 'https://www.flightradar24.com/data/airports/abu/arrivals',
    'Babo Airport': 'https://www.flightradar24.com/data/airports/bxb/arrivals',
    'Bajawa Turelelo Soa Airport': 'https://www.flightradar24.com/data/airports/bjw/arrivals',
    'Balikpapan Sepinggan Airport': 'https://www.flightradar24.com/data/airports/bpn/arrivals',
    'Banda Aceh International Airport': 'https://www.flightradar24.com/data/airports/btj/arrivals',
    'Bandar Lampung Radin Inten II Airport': 'https://www.flightradar24.com/data/airports/tkg/arrivals',
    'Bandung Husein Sastranegara International Airport': 'https://www.flightradar24.com/data/airports/bdo/arrivals',
    'Banjarmasin Syamsudin Noor Airport': 'https://www.flightradar24.com/data/airports/bdj/arrivals',
    'Batam Hang Nadim Airport': 'https://www.flightradar24.com/data/airports/bth/arrivals',
    'Batu Licin Airport': 'https://www.flightradar24.com/data/airports/btw/arrivals',
    'Bau-Bau Betoambari Airport': 'https://www.flightradar24.com/data/airports/buw/arrivals',
    'Bengkulu Fatmawati Soekarno Airport': 'https://www.flightradar24.com/data/airports/bks/arrivals',
    'Biak Frans Kaisiepo Airport': 'https://www.flightradar24.com/data/airports/bik/arrivals',
    'Bima Sultan Muhammad Salahudin Airport': 'https://www.flightradar24.com/data/airports/bmu/arrivals',
    'Blimbingsari Airport': 'https://www.flightradar24.com/data/airports/bwx/arrivals',
    'Buol Airport': 'https://www.flightradar24.com/data/airports/uol/arrivals',
    'Dekai Nop Goliat Airport': 'https://www.flightradar24.com/data/airports/dex/arrivals',
    'Denpasar Ngurah Rai International Airport': 'https://www.flightradar24.com/data/airports/dps/arrivals',
    'Dumai Pinang Kampai Airport': 'https://www.flightradar24.com/data/airports/dum/arrivals',
    'Ende H. Hasan Aroeboesman Airport': 'https://www.flightradar24.com/data/airports/ene/arrivals',
    'Fakfak Torea Airport': 'https://www.flightradar24.com/data/airports/fkq/arrivals',
    'Gorontalo Jalaluddin Airport': 'https://www.flightradar24.com/data/airports/gto/arrivals',
    'Gunung Sitoli Binaka Airport': 'https://www.flightradar24.com/data/airports/gns/arrivals',
    'Jakarta Halim Perdanakusuma Airport': 'https://www.flightradar24.com/data/airports/hlp/arrivals',
    'Jakarta Soekarno Hatta International Airport': 'https://www.flightradar24.com/data/airports/cgk/arrivals',
    'Jambi Sultan Thaha Airport': 'https://www.flightradar24.com/data/airports/djb/arrivals',
    'Jayapura Sentani Airport': 'https://www.flightradar24.com/data/airports/djj/arrivals',
    'Jember Notohadinegoro Airport': 'https://www.flightradar24.com/data/airports/jbb/arrivals',
    'Kaimana Utarom Airport': 'https://www.flightradar24.com/data/airports/kng/arrivals',
    'Kalimarau Airport': 'https://www.flightradar24.com/data/airports/bej/arrivals',
    'Kebar Airport': 'https://www.flightradar24.com/data/airports/keq/arrivals',
    'Kendari Haluoleo Airport': 'https://www.flightradar24.com/data/airports/kdi/arrivals',
    'Ketapang Airport': 'https://www.flightradar24.com/data/airports/ktg/arrivals',
    'Kotabaru Gusti Syamsir Alam Airport': 'https://www.flightradar24.com/data/airports/kbu/arrivals',
    'Kupang El Tari Airport': 'https://www.flightradar24.com/data/airports/koe/arrivals',
    'Labuan Bajo Komodo Airport': 'https://www.flightradar24.com/data/airports/lbj/arrivals',
    'Labuha Oesman Sadik Airport': 'https://www.flightradar24.com/data/airports/lah/arrivals',
    'Langgur Karel Sadsuitubun Airport': 'https://www.flightradar24.com/data/airports/luv/arrivals',
    'Larantuka Gewayantana Airport': 'https://www.flightradar24.com/data/airports/lka/arrivals',
    'Lewoleba Wunopito Airport': 'https://www.flightradar24.com/data/airports/lwe/arrivals',
    'Lhokseumawe Malikus Saleh Airport': 'https://www.flightradar24.com/data/airports/lsw/arrivals',
    'Lombok International Airport': 'https://www.flightradar24.com/data/airports/lop/arrivals',
    'Lubuklinggau Silampari Airport': 'https://www.flightradar24.com/data/airports/llj/arrivals',
    'Luwuk Bubung Airport': 'https://www.flightradar24.com/data/airports/luw/arrivals',
    'Majalengka Kertajati International Airport': 'https://www.flightradar24.com/data/airports/kjt/arrivals',
    'Makassar Sultan Hasanuddin International Airport': 'https://www.flightradar24.com/data/airports/upg/arrivals',
    'Malang Abdul Rachman Saleh Airport': 'https://www.flightradar24.com/data/airports/mlg/arrivals',
    'Malinau Kolonel RA Bessing Airport': 'https://www.flightradar24.com/data/airports/lnu/arrivals',
    'Mamuju Tampa Padang Airport': 'https://www.flightradar24.com/data/airports/mju/arrivals',
    'Manado Sam Ratulangi International Airport': 'https://www.flightradar24.com/data/airports/mdc/arrivals',
    'Manokwari Rendani Airport': 'https://www.flightradar24.com/data/airports/mkw/arrivals',
    'Matak Tarempa Airport': 'https://www.flightradar24.com/data/airports/mwk/arrivals',
    'Maumere Frans Seda Airport': 'https://www.flightradar24.com/data/airports/mof/arrivals',
    'Medan Kuala Namu International Airport': 'https://www.flightradar24.com/data/airports/kno/arrivals',
    'Melangguane Airport': 'https://www.flightradar24.com/data/airports/mna/arrivals',
    'Merauke Mopah International Airport': 'https://www.flightradar24.com/data/airports/mkq/arrivals',
    'Muara Bungo Airport': 'https://www.flightradar24.com/data/airports/buu/arrivals',
    'Nabire Airport': 'https://www.flightradar24.com/data/airports/nbx/arrivals',
    'Nanga Pinoh Airport': 'https://www.flightradar24.com/data/airports/npo/arrivals',
    'Nunukan Airport': 'https://www.flightradar24.com/data/airports/nnx/arrivals',
    'Oksibil Airport': 'https://www.flightradar24.com/data/airports/okl/arrivals',
    'Padang Minangkabau International Airport': 'https://www.flightradar24.com/data/airports/pdg/arrivals',
    'Palangkaraya Tjilik Riwut Airport': 'https://www.flightradar24.com/data/airports/pky/arrivals',
    'Palembang International Airport': 'https://www.flightradar24.com/data/airports/plm/arrivals',
    'Palopo Lagaligo Airport': 'https://www.flightradar24.com/data/airports/llo/arrivals',
    'Palu Mutiara Airport': 'https://www.flightradar24.com/data/airports/plw/arrivals',
    'Pangkal Pinang Airport': 'https://www.flightradar24.com/data/airports/pgk/arrivals',
    'Pangkalan Bun Iskandar Airport': 'https://www.flightradar24.com/data/airports/pkn/arrivals',
    'Pekanbaru Sultan Syarif Kasim II Airport': 'https://www.flightradar24.com/data/airports/pku/arrivals',
    'Pomala Airport': 'https://www.flightradar24.com/data/airports/pum/arrivals',
    'Pontianak Supadio Airport': 'https://www.flightradar24.com/data/airports/pnk/arrivals',
    'Putussibau Pangsuma Airport': 'https://www.flightradar24.com/data/airports/psu/arrivals',
    'Raha Sugimanuru Airport': 'https://www.flightradar24.com/data/airports/raq/arrivals',
    'Ranai Airport': 'https://www.flightradar24.com/data/airports/ntx/arrivals',
    'Rengat Japura Airport': 'https://www.flightradar24.com/data/airports/rgt/arrivals',
    'Roti David C. Saudale Airport': 'https://www.flightradar24.com/data/airports/rti/arrivals',
    'Ruteng Frans Sales Lega Airport': 'https://www.flightradar24.com/data/airports/rtg/arrivals',
    'Sabang Maimun Saleh Airport': 'https://www.flightradar24.com/data/airports/sbg/arrivals',
    'Samarinda AP Tumenggung Pranoto Airport': 'https://www.flightradar24.com/data/airports/aap/arrivals',
    'Sampit Airport': 'https://www.flightradar24.com/data/airports/smq/arrivals',
    'Saumlaki Mathilda Batlayeri Airport': 'https://www.flightradar24.com/data/airports/sxk/arrivals',
    'Selayar Islands H. Aroeppala Airport': 'https://www.flightradar24.com/data/airports/ksr/arrivals',
    'Semarang Achmad Yani International Airport': 'https://www.flightradar24.com/data/airports/srg/arrivals',
    'Sibolga Ferdinand Lumban Tobing Airport': 'https://www.flightradar24.com/data/airports/flz/arrivals',
    'Siborong-Borong Silangit Airport': 'https://www.flightradar24.com/data/airports/dtb/arrivals',
    'Sintang Airport': 'https://www.flightradar24.com/data/airports/sqg/arrivals',
    'Sorong Dominique Edward Osok Airport': 'https://www.flightradar24.com/data/airports/soq/arrivals',
    'Sumbawa Besar Airport': 'https://www.flightradar24.com/data/airports/swq/arrivals'
}

airport_name = []
times = []
dates = []
flight = []
flightfrom = []
airlines = []
aircrafts = []
flight_status = []
abbrs = []
for key, value in urls1.items():
    driver.get(value)
    time.sleep(10)
    scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Time
    time_div = soup.find_all('div', {'class': 'col-xs-3 col-sm-3 p-xxs'})
    for a in time_div:
        time_span = a.find_all('span', {'class': 'ng-binding'})
        for b in time_span:
            time_text = b.text.strip()
            times.append(time_text)

    # Date
    date_tr = soup.find_all('tr', {'class': 'hidden-xs hidden-sm ng-scope'})
    for d in date_tr:
        date = d.get('data-date')
        dates.append(date)

    # flight
    flight_td = soup.find_all('td', {'class': 'p-l-s cell-flight-number'})
    for a in flight_td:
        aflight = a.find_all('a', {'class': 'notranslate ng-binding'})
        for b in aflight:
            flight_text = b.get('title')
            flight.append(flight_text)

    # from
    asal = [link.get_text().strip() for link in soup.find_all("span", {"class": "hide-mobile-only ng-binding"})]
    flightfrom.extend(asal)

    abbreviation = soup.find_all('div', {'ng-show': '(objFlight.flight.airport.origin)'})
    for a in abbreviation:
        abbr_a = a.find_all('a', {'class': 'fs-10 fbold notranslate ng-binding'})
        for b in abbr_a:
            abbr_text = b.text.strip()
            abbrs.append(abbr_text)

    # airline
    airline_td = soup.find_all('td', {'class': 'cell-airline'})
    for a in airline_td:
        airline_a = a.find_all('a', {'class': 'notranslate ng-binding'})
        for b in airline_a:
            airline = b.get('title')
            airlines.append(airline)

    # aircraft
    aircraft_td = soup.find_all('td')
    for a in aircraft_td:
        aircraft_span = a.find_all('span', {'class': 'notranslate ng-binding'})
        for b in aircraft_span:
            aircraft = b.text.strip()
            aircrafts.append(aircraft)

    # flight_status
    status_td = soup.find_all('td', {'class': 'ng-binding'})
    for a in status_td:
        status_span = a.find_all('span', {'class': 'ng-binding'})
        for b in status_span:
            status = b.text.strip()
            flight_status.append(status)

    airport_tmp = [key] * len(asal)
    airport_name.extend(airport_tmp)

print(airport_name)
df1 = pd.DataFrame()
df1["Dates"] = dates
df1["Time"] = times
df1["Flight"] = flight
df1["From"] = list(map(' '.join, zip(flightfrom, abbrs)))
df1["Airlines"] = airlines
df1["Aircrafts"] = aircrafts
df1["Status"] = flight_status
df1["Airport"] = airport_name