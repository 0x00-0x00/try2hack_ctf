#!/usr/bin/env python

#import requests # Replaced by CloudFlare scraper
import cfscrape


def generate_url(ocx_name):
    initial = ocx_name[0:1]
    return("https://ocxdump.com/ocxfiles/{0}/{1}".format(initial, ocx_name.upper()))

def download_file(link):
    local_file = link.split('/')[-1]
    scraper = cfscrape.create_scraper()
    data = scraper.get(link).content
    with open(local_file, "wb") as f:
        f.write(data)
    print("Downloaded {0} bytes.".format(len(data)))
    return 0

def main():
    input_data = raw_input("Digite o link do ocx: ")
    link_gerado = generate_url(input_data)

    print("Link gerado: {0}".format(link_gerado))
    download_file(link_gerado)
    return 0


if __name__ == "__main__":
    main()
